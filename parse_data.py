import data
from jobs.models import Company, Specialty, Vacancy

specialties = []
for specialty in data.specialties:
    temp = Specialty(
        title=specialty['title'],
        code=specialty['code']
    )
    specialties.append(temp)
    temp.save()

companies = []
for company in data.companies:
    temp = Company(
        name=company['title'],
        logo=company['logo'],
        employee_count=int(company['employee_count']),
        location=company['location'],
        description=company['description']
    )
    companies.append(temp)
    temp.save()

jobs = []
for job in data.jobs:
    temp = Vacancy(
        title=job['title'],
        specialty=Specialty.objects.get(code=job['specialty']),
        company=Company.objects.get(id=int(job['company'])),
        salary_min=int(job['salary_from']),
        salary_max=int(job['salary_to']),
        # published_at=datetime.datetime.strptime(job['posted'], '%Y-%m-%d'),
        published_at=job['posted'],
        skills=job['skills'],
        description=job['description']
    )
    jobs.append(temp)
    temp.save()
