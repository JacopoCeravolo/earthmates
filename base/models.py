from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Startup(models.Model):
    NONE = "NONE"

    BUSINESS_ANGELS = "BUSINESS_ANGELS"
    VC = "VC"
    FAMILY_OFFICE = "FAMILY_OFFICE"
    FOUNDATION = "FOUNDATION"
    ALL_INVESTOR = "ALL_INVESTOR"

    INVESTOR_TYPE_CHOICES = (
        (BUSINESS_ANGELS, "Business Angels"),
        (VC, "VCs"),
        (FAMILY_OFFICE, "Family Office"),
        (FOUNDATION, "Foundation"),
        (ALL_INVESTOR, "All of them"),
    )

    ACCOUNTING = "ACCOUNTING"
    CONTROLLING = "CONTROLLING"
    FUNDRAISING = "FUNDRAISING"
    HR = "HR"
    LEGAL = "LEGAL"
    LOGISTICS = "LOGISTICS"
    MANAGEMENT = "MANAGEMENT"
    MARKTING = "MARKTING"
    PR = "PR"
    PROCUREMENT = "PROCUREMENT"
    PRODUCT_DEVELOPEMENT = "PRODUCT_DEVELOPEMENT"
    PRODUCTION = "PRODUCTION"
    SALES = "SALES"
    STRATEGY = "STRATEGY"
    TECHNOLOGY = "TECHNOLOGY"

    INVESTOR_EXPERTISE_CHOICES = (
        (ACCOUNTING, "Accounting"),
        (CONTROLLING, "Controlling"),
        (FUNDRAISING, "Fundraising"),
        (HR, "HR"),
        (LEGAL, "Legal"),
        (LOGISTICS, "Logistics"),
        (MANAGEMENT, "Management"),
        (MARKTING, "Marketing"),
        (PR, "PR"),
        (PROCUREMENT, "Procurement"),
        (PRODUCT_DEVELOPEMENT, "Product Development"),
        (PRODUCTION, "Production"),
        (SALES, "Sales"),
        (STRATEGY, "Strategy"),
        (TECHNOLOGY, "Technology"),
        (NONE, "None"),
    )

    HAS_CONTACTS = "HAS_CONTACT"
    KNOWS_INDUSTRY = "KNOWS_INDUSTRY"
    HAS_VISION = "HAS_VISION"
    COVER_VALUES = "COVER_VALUES"
    KNOWS_TECH = "KNOWS_TECH"
    HAS_IMPACT = "HAS_IMPACT"


    INVESTOR_VALUE_CHOICES = (
        (HAS_CONTACTS, "he brings a lot of contacts with him"),
        (KNOWS_INDUSTRY, "he knows your industry very well"),
        (HAS_VISION, "he he represents my vision"),
        (COVER_VALUES, "covers my values"),
        (KNOWS_TECH, "has technical know-how"),
        (HAS_IMPACT, "we share the same impact thought"),
        (NONE, "None"),
    )

    SOUTH_AFRICA = "SOUTH_AFRICA"
    RWANDA = "RWANDA"

    LOCATION_CHOICES = ((SOUTH_AFRICA, "South Africa"), (RWANDA, "Rwanda"))

    PRE_SEED = "PRE_SEED"
    SEED = "SEED"
    SERIES_A = "SERIES_A"
    SERIES_B = "SERIES_B"
    SERIES_C = "SERIES_C"

    STAGE_CHOICES = (
        (PRE_SEED, "Pre-Seed"),
        (SEED, "Seed"),
        (SERIES_A, "Series A"),
        (SERIES_B, "Series B"),
        (SERIES_C, "Series C"),
    )

    REAL_ESTATE = "REAL_ESTATE"
    NATURE_PROTECTION = "NATURE_PROTECTION"
    WOMAN_EMPOWERMENT = "WOMAN_EMPOWERMENT"
    POVERTY_ALLEVIATION = "POVERTY_ALLEVIATION"
    GREENTECH = "GREENTECH"
    SMART_CITY = "SMART_CITY"
    MOBILITY = "MOBILITY"
    ENERGY = "ENERGY"
    EDUCATION = "EDUCATION"
    HEALTH = "HEALTH"
    SPORTS = "SPORTS"
    COSMETICS = "COSMETICS"
    FINANCIAL_AND_INSURANCE = "FINANCIAL_AND_INSURANCE"
    FOOD = "FOOD"
    LEGAL_SERVICES = "LEGAL_SERVICES"
    RENTAL_AND_REPAIR = "RENTAL_AND_REPAIR"
    TRANSPORTATION_AND_STORAGE = "TRANSPORTATION_AND_STORAGE"
    INFORMATION_AND_COMMUNICATION = "INFORMATION_AND_COMMUNICATION"
    ARTS_ENTERTAINMENT_AND_RECREATION = "ENTERTAINMENT_AND_RECREATION"
    SUPPORT_SERVICES = "SUPPORT_SERVICES"
    TECHNICAL_SERVICES = "TECHNICAL_SERVICES"
    ENVIRONMENTAL_CONSULTING = "ENVIRONMENTAL_CONSULTING"
    OTHER = "OTHER"

    INDUSTRY_CHOICES = (
        (REAL_ESTATE, "Real Estate"),
        (NATURE_PROTECTION, "Nature Protection"),
        (WOMAN_EMPOWERMENT, "Woman Empowerment"),
        (POVERTY_ALLEVIATION, "Poverty Alleviation"),
        (GREENTECH, "Greentech"),
        (SMART_CITY, "Smart City"),
        (MOBILITY, "Mobility"),
        (ENERGY, "Energy"),
        (EDUCATION, "Education"),
        (HEALTH, "Health"),
        (SPORTS, "Sports"),
        (COSMETICS, "Cosmetics"),
        (FINANCIAL_AND_INSURANCE, "Financial & Insurance"),
        (FOOD, "Food"),
        (LEGAL_SERVICES, "Legal"),
        (RENTAL_AND_REPAIR, "Rental & Repair"),
        (TRANSPORTATION_AND_STORAGE, "Transportation & Storage"),
        (INFORMATION_AND_COMMUNICATION, "Information & Communication"),
        (ARTS_ENTERTAINMENT_AND_RECREATION, "Arts, Entertainment & Recreation"),
        (SUPPORT_SERVICES, "Support Services"),
        (TECHNICAL_SERVICES, "Technical Services"),
        (ENVIRONMENTAL_CONSULTING, "Environmental Consulting"),
        (OTHER, "Other"),
        (NONE, "None"),
    )

    B2B = "B2B"
    B2C = "B2C"
    CONSULTANCY = "CONSULTANCY"
    FOR_PROFIT = "FOR_PROFIT"
    NON_PROFIT = "NON_PROFIT"

    BUSINESS_TYPE_CHOICES = (
        (B2B, "B2B"),
        (B2C, "B2C"),
        (CONSULTANCY, "Consultancy"),
        (FOR_PROFIT, "For Profit"),
        (NON_PROFIT, "Non Profit"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    startup_name = models.CharField(max_length=50, unique=True, default="")

    investor_type = models.CharField(
        max_length=20, choices=INVESTOR_TYPE_CHOICES, default=ALL_INVESTOR
    )
    investor_expertise = models.CharField(
        max_length=20, choices=INVESTOR_EXPERTISE_CHOICES, default=NONE
    )
    investor_value = models.CharField(
        max_length=20, choices=INVESTOR_VALUE_CHOICES, default=NONE
    )
    capital_required = models.IntegerField(default=100000)

    location = models.CharField(
        max_length=20, choices=LOCATION_CHOICES, default=SOUTH_AFRICA
    )
    stage = models.CharField(
        max_length=10, choices=STAGE_CHOICES, default=PRE_SEED
    )
    industry = models.CharField(
        max_length=30, choices=INDUSTRY_CHOICES, default=NONE
    )
    business_type = models.CharField(
        max_length=20, choices=BUSINESS_TYPE_CHOICES, default=B2B
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.startup_name
    
