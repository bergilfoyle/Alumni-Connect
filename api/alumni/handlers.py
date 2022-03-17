import pandas as pd
from datetime import datetime
from django.contrib.auth.models import User, Group
from alumni.models import Alumni, Placements

def handle_alumni_csv(file):
    data = pd.read_csv(file)
    try:
        for _, row in data.iterrows():
            usn = row['USN']
            name = row['Name']
            phone = row['Phone']
            email = row['RV Email']
            year = email[len(email)-14:len(email)-12]
            branch = row['Department']
            year_joined = datetime.strptime(year, '%y').date()
            year_passed = datetime.strptime(str(int(year) + 4), '%y')
            personal_email = row['Personal Email']
            company_name = row['Company Name']
            ctc = row['CTC']
            type = row['Type']
            job_profile = row['Job Profile']

            group = Group.objects.get(name='alumni')
            user, _ = User.objects.get_or_create(email = email)
            user.username = email[:len(email)-12]
            user.set_password('anteater')
            user.groups.add(group)
            user.save()

            if Alumni.objects.filter(usn = usn).exists():
                alumnus = Alumni.objects.get(usn=usn)
            else:
                alumnus = Alumni.objects.create(usn = usn, user = user)
            alumnus.user = user
            alumnus.name = name
            alumnus.phone = phone
            alumnus.email = email
            alumnus.personal_email = personal_email
            alumnus.year_joined = year_joined
            alumnus.year_passed = year_passed
            alumnus.branch = branch
            alumnus.save()
            
            placement, _ = Placements.objects.get_or_create(alumnus = alumnus)
            placement.company_name = company_name
            placement.job_profile = job_profile
            placement.ctc = ctc
            placement.type = type
            placement.save()
        return True
    except Exception as e:
        print(e)
        return False
