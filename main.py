import itertools
from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Extract form data
        company_names = request.form.get('company_names').split(',')
        years = request.form.get('years').split(',')
        project_names = request.form.get('project_names').split(',')
        departments = request.form.get('departments').split(',')
        cities = request.form.get('cities').split(',')

        # Generate passwords
        passwords = generate_passwords(company_names, years, project_names, departments, cities)
        
        # Render passwords to the user
        return render_template_string("""
            <!DOCTYPE html>
            <html>
            <body>
                <h2>Generated Passwords</h2>
                <ul>
                {% for password in passwords %}
                    <li>{{ password }}</li>
                {% endfor %}
                </ul>
                <a href="/">Generate New Passwords</a>
            </body>
            </html>
        """, passwords=passwords)
    else:
        # Render home page with form
        return render_template_string("""
            <!DOCTYPE html>
            <html>
            <head>
                <title>Password Generator</title>
            </head>
            <body>
                <h2>Enter Details to Generate Passwords</h2>
                <form method="post">
                    Company Names: <input type="text" name="company_names"><br>
                    Years: <input type="text" name="years"><br>
                    Project Names: <input type="text" name="project_names"><br>
                    Departments: <input type="text" name="departments"><br>
                    Cities: <input type="text" name="cities"><br>
                    <input type="submit" value="Generate Passwords">
                </form>
            </body>
            </html>
        """)

def generate_passwords(company_names, years, project_names, departments, cities):
    passwords = []
    
    # Generate passwords with specified capitalization variations for company names
    for company_name in company_names:
        # Trim and generate variations
        company_name = company_name.strip()
        variations = [
            company_name.lower(),  # No caps
            company_name.upper(),  # All caps
            company_name.capitalize()  # First cap
        ]
        
        for variation in variations:
            for year in years:
                passwords.extend([
                    f"{variation}123",
                    f"{variation}!",
                    f"{variation}{year.strip()}",
                    f"{year.strip()}{variation}!",
                    f"PasswordFor{variation}",
                ])

    # Add other passwords (keeping these simple for clarity)
    for project_name in project_names:
        passwords.append(f"{project_name.strip()}!")
    
    for department in departments:
        passwords.append(f"{department.strip()}123")
    
    for city in cities:
        passwords.append(f"{city.strip()}Office")

    # Additional static passwords
    passwords.extend([
        "Welcome1",
        "Password1234",
        "LetMeIn!",
        "1234567890",
        "ChangeMe",
        "1234QWER",
        "TempPass1",
        "Guest1234",
        "AdminPassword"
    ])

    return set(passwords)  # Use set to remove duplicates

# The rest of the Flask application code remains unchanged


# The rest of the Flask application remains unchanged
if __name__ == '__main__':
    app.run(debug=True)

