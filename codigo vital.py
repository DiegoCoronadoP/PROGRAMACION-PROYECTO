# Import necessary libraries
import re

# Define a function that takes in user data as input
def analyze_user_data(job_field, skills, courses, experiences, gender, age):
    # Initialize an empty list to store job recommendations
    job_recommendations = []

    # Define a dictionary of job fields and corresponding skills
    job_skills = {
        "software engineering": ["programming", "software development", "software testing"],
        "data science": ["data analysis", "machine learning", "statistics"],
        "marketing": ["social media", "SEO", "content creation"],
        "design": ["graphic design", "UX/UI design", "illustration"],
        "finance": ["accounting", "financial analysis", "investment banking"],
        "human resources": ["recruitment", "talent management", "benefits administration"],
        "operations management": ["supply chain management", "logistics", "process improvement"],
        "business development": ["market research", "competitive analysis", "strategic planning"],
        "project management": ["agile methodologies", "project planning", "risk management"],
        "customer service": ["customer support", "customer retention", "conflict resolution"],
        "sales": ["sales strategy", "account management", "negotiation"],
        "networking": ["network architecture", "network security", "network administration"],
        "database administration": ["database design", "database development", "database management"],
        "artificial intelligence": ["machine learning", "natural language processing", "computer vision"],
        "cybersecurity": ["security analysis", "penetration testing", "incident response"],
        "data analysis": ["data visualization", "statistical analysis", "data mining"],
        "digital marketing": ["SEO", "PPC", "social media marketing"],
        "electrical engineering": ["circuit design", "microcontrollers", "electrical systems"],
        "mechanical engineering": ["mechanical design", "thermal systems", "mechanical systems"],
        "civil engineering": ["structural analysis", "construction management", "transportation engineering"]
    }

    # Iterate through the job fields and corresponding skills
    for field, skills_list in job_skills.items():
        # Check if the user's skills match the skills required for the job field
        if set(skills).intersection(skills_list):
            # If there is a match, add the job field to the list of job recommendations
            job_recommendations.append(field)

    # Define a dictionary of job titles and corresponding courses
    job_courses = {
        "software engineer": ["Introduction to Computer Science", "Data Structures and Algorithms", "Software Engineering"],
        "data scientist": ["Introduction to Data Science", "Machine Learning", "Deep Learning"],
        "marketing specialist": ["Social Media Marketing", "SEO", "Content Marketing"],
        "graphic designer": ["Graphic Design", "UX/UI Design", "Illustration"],
        "financial analyst": ["Financial Accounting", "Financial Management", "Investment Analysis"],
        "human resources manager": ["Human Resource Management", "Organizational Behavior", "Benefits Administration"],
        "operations manager": ["Operations Management", "Supply Chain Management", "Process Improvement"],
        "business development manager": ["Business Development", "Market Research", "Competitive Analysis"],
        "project manager": ["Project Management", "Agile Methodologies", "Risk Management"],
        "customer service representative": ["Customer Service", "Customer Support", "Conflict Resolution"],
        "sales representative": ["Sales Strategy", "Account Management", "Negotiation"],
        "network administrator": ["Network Administration", "Network Security", "Network Architecture"],
        "database administrator": ["Database Administration", "Database Design", "Database Development"],
        "artificial intelligence engineer": ["Artificial Intelligence", "Machine Learning", "Natural Language Processing"],
        "cybersecurity specialist": ["Cybersecurity", "Security Analysis", "Penetration Testing"],
        "data analyst": ["Data Analysis", "Data Visualization", "Statistical Analysis"],
        "digital marketing specialist": ["Digital Marketing", "SEO", "PPC"],
        "electrical engineer": ["Electrical Engineering", "Circuit Design", "Microcontrollers"],
        "mechanical engineer": ["Mechanical Engineering", "Mechanical Design", "Thermal Systems"],
        "civil engineer": ["Civil Engineering", "Structural Analysis", "Construction Management"]
    }

    # Iterate through the job titles and corresponding courses
    for title, courses_list in job_courses.items():
        # Check if the user's courses match the courses required for the job title
        if set(courses).intersection(courses_list):
            # If there is a match, add the job title to the list of job recommendations
            job_recommendations.append(title)

    # Define a dictionary of job titles and corresponding experiences
    # Define a dictionary of job titles and corresponding experiences
    job_experiences = {
        "software engineer": ["software development", "programming", "software testing"],
        "data scientist": ["data analysis", "machine learning", "statistics"],
        "marketing specialist": ["social media", "SEO", "content creation"],
        "graphic designer": ["graphic design", "UX/UI design", "illustration"],
        "financial analyst": ["financial analysis", "financial modeling", "investment analysis"],
        "human resources manager": ["recruitment", "talent management", "benefits administration"],
        "operations manager": ["supply chain management", "logistics", "process improvement"],
        "business development manager": ["market research", "competitive analysis", "strategic planning"],
        "project manager": ["project management", "agile methodologies", "risk management"],
        "customer service representative": ["customer support", "customer retention", "conflict resolution"],
        "sales representative": ["sales strategy", "account management", "negotiation"],
        "network administrator": ["network architecture", "network security", "network administration"],
        "database administrator": ["database design", "database development", "database management"],
        "artificial intelligence engineer": ["machine learning", "natural language processing", "computer vision"],
        "cybersecurity specialist": ["security analysis", "penetration testing", "incident response"],
        "data analyst": ["data visualization", "statistical analysis", "data mining"],
        "digital marketing specialist": ["SEO", "PPC", "social media marketing"],
        "electrical engineer": ["circuit design", "microcontrollers", "electrical systems"],
        "mechanical engineer": ["mechanical design", "thermal systems", "mechanical systems"],
        "civil engineer": ["structural analysis", "construction management", "transportation engineering"]
       
    }

    # Iterate through the job titles and corresponding experiences
    for title, experiences_list in job_experiences.items():
    # Check if the user's experiences match the experiences required for the job title
        if set(experiences).intersection(experiences_list):
        # If there is a match, add the job title to the list of job recommendations
            job_recommendations.append(title)

# Define a dictionary of job titles and corresponding gender and age requirements
    job_requirements = {
        "software engineer": {"gender": "any", "age": "18-35"},
        "data scientist": {"gender": "any", "age": "25-40"},
        "marketing specialist": {"gender": "any", "age": "22-30"},
        "graphic designer": {"gender": "any", "age": "20-35"},
        "financial analyst": {"gender": "any", "age": "25-40"},
        "human resources manager": {"gender": "any", "age": "30-45"},
        "operations manager": {"gender": "any", "age": "30-45"},
        "business development manager": {"gender": "any", "age": "30-45"},
        "project manager": {"gender": "any", "age": "30-45"},
        "customer service representative": {"gender": "any", "age": "18-30"},
        "sales representative": {"gender": "any", "age": "25-40"},
        "network administrator": {"gender": "any", "age": "25-40"},
        "database administrator": {"gender": "any", "age": "25-40"},
        "artificial intelligence engineer": {"gender": "any", "age": "25-40"},
        "cybersecurity specialist": {"gender": "any", "age": "25-40"},
        "data analyst": {"gender": "any", "age": "25-40"},
        "digital marketing specialist": {"gender": "any", "age": "22-30"},
        "electrical engineer": {"gender": "any", "age": "25-40"},
        "mechanical engineer": {"gender": "any", "age": "25-40"},
        "civil engineer": {"gender": "any", "age": "25-40"}
}
    # Iterate through the job titles and corresponding 
    for title, requirements in job_requirements.items():
        if gender == requirements["gender"] and age >= int(requirements["age"].split("-")[0]) and age <= int(requirements["age"].split("-")[1]):
        # If there is a match, add the job title to the list of job recommendations
           job_recommendations.append(title)
        # Return the list of job recommendations
    return job_recommendations
    # Check if the user's gender and age match the requirements for the job title
    

# Get user data
# Get user data
job_field = input("Enter your job field: ")
skills = input("Enter your skills (separated by commas): ").split(",")
courses = input("Enter the courses you have taken (separated by commas): ").split(",")
experiences = input("Enter your work experiences (separated by commas): ").split(",")
gender = input("Enter your gender: ")
age = int(input("Enter your age: "))

# Analyze user data and get job recommendations
job_recommendations = analyze_user_data(job_field, skills, courses, experiences, gender, age)

# Print job recommendations
print("Job recommendations:")
for recommendation in job_recommendations:
    print(recommendation)







