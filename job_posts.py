# from linkedin_api import Linkedin
# username = 'ksseena30@gmail.com'
# password = '9066949892'
# api = Linkedin(username, password)

# Assuming you have a valid LinkedIn username, not URL
# 1.neel-raval
# 2.linkedin.com/in/sunaina-hanjura-51398314
# 3.linkedin.com/in/sfehr
# profile_username = "sunaina-hanjura-51398314"

# profile_info = api.get_profile(profile_username)
# posts = api.get_profile_posts(profile_username)
# print(posts)


from linkedin_api import Linkedin
import json

def extract_jobs_from_posts(posts):
    jobs_list = []

    for post in posts:
        job_description = None
        job_title = None
        job_company = None
        job_location = None
        post_data = json.loads(json.dumps(post))
       
        commentary = post_data.get('commentary', {}).get('text', {}).get('text','')
        if "#hiring" in commentary or "hiring" in commentary or "Looking" in commentary:
            job_description = commentary

        if job_description:
            content = post_data.get('content', {}).get('com.linkedin.voyager.feed.render.EntityComponent', {})
            job_title = content.get('title', {}).get('text', None)

            attributes = content.get('image', {}).get('attributes', [])
            if attributes and 'miniCompany' in attributes[0]:
                job_company = attributes[0]['miniCompany'].get('name', None)

            job_location = content.get('description', {}).get('text', None)

            jobs_list.append((job_description, job_title, job_company, job_location))

    return jobs_list


import json
username = 'ksseena30@gmail.com'
password = '9066949892'
api = Linkedin(username, password)
profile_usernames = ["naveenkumars1003","sunaina-hanjura-51398314", "neel-raval", "sunaina-hanjura-51398314", "sfehr", "chandra-cogentnext"]
all_jobs_list = []


for profile_username in profile_usernames:
    try:
        posts = api.get_profile_posts(profile_username)
        jobs_list = extract_jobs_from_posts(posts)
        all_jobs_list.extend(jobs_list)
    except Exception as e:
        print(f"Failed to access profile {profile_username}: {e}")


# posts = api.get_profile_posts("sunaina-hanjura-51398314")
# if posts: 
#     # print(json.dumps(posts))
#     print(json.dumps(posts, indent=4))

# # Print or process the job details stored in the overall list
for job in all_jobs_list:
    job_description, job_title, job_company, job_location = job
    print("Job Description:", job_description)
    print("Job Title:", job_title)
    print("Job Company:", job_company)
    print("Job Location:", job_location)
    print("-" + "-"*50 + "-")