
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from uvicorn import run as app_run


from us_visa.constant import APP_HOST, APP_PORT
from us_visa.pipeline.prediction_pipeline import USvisaData, USvisaClassifier
from us_visa.pipeline.training_pipeline import TrainPipeline

app = FastAPI()


origins = ["*"]  

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class VisaRequest(BaseModel):
    continent: str
    education_of_employee: str
    has_job_experience: str
    requires_job_training: str
    no_of_employees: str
    company_age: str
    region_of_employment: str
    prevailing_wage: str
    unit_of_wage: str
    full_time_position: str

@app.post("/predict")
async def predict(data: VisaRequest):
    try:
        usvisa_data = USvisaData(
            continent=data.continent,
            education_of_employee=data.education_of_employee,
            has_job_experience=data.has_job_experience,
            requires_job_training=data.requires_job_training,
            no_of_employees=data.no_of_employees,
            company_age=data.company_age,
            region_of_employment=data.region_of_employment,
            prevailing_wage=data.prevailing_wage,
            unit_of_wage=data.unit_of_wage,
            full_time_position=data.full_time_position,
        )

        usvisa_df = usvisa_data.get_usvisa_input_data_frame()
        model_predictor = USvisaClassifier()
        value = model_predictor.predict(dataframe=usvisa_df)[0]

        status = "Visa Approved ✅" if value == 1 else "Visa Not Approved ❌"
        return {"result": status}

    except Exception as e:
        return {"error": str(e)}

@app.get("/train")
async def train():
    try:
        pipeline = TrainPipeline()
        pipeline.run_pipeline()
        return {"message": "Training successful!"}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    app_run(app, host=APP_HOST, port=APP_PORT)

