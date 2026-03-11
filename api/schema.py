from pydantic import BaseModel

class CustomerData(BaseModel):

    gender: int
    SeniorCitizen: int
    Partner: int
    Dependents: int
    tenure: int
    PhoneService: int
    PaperlessBilling: int

    MonthlyCharges: float
    TotalCharges: float

    MultipleLines_No_phone_service: int = 0
    MultipleLines_Yes: int = 0

    InternetService_Fiber_optic: int = 0
    InternetService_No: int = 0

    OnlineSecurity_Yes: int = 0
    OnlineBackup_Yes: int = 0
    DeviceProtection_Yes: int = 0
    TechSupport_Yes: int = 0

    StreamingTV_Yes: int = 0
    StreamingMovies_Yes: int = 0

    Contract_One_year: int = 0
    Contract_Two_year: int = 0

    PaymentMethod_Credit_card_automatic: int = 0
    PaymentMethod_Electronic_check: int = 0
    PaymentMethod_Mailed_check: int = 0