The relevant code from the message is a Python script:

```python
# Step 1: Identify the Issue
issue_type = "SQL Injection"

# Step 2: Locate Source Files
source_file_sql_injection = "/src/main/java/com/example/app/DatabaseManager.java"

# Step 3: Pinpoint Affected Code
commit = "abc123df"

# Step 4: Special Configuration Requirements
special_config_sql = None

# Step 5: Specify Reproduction Steps
reproduction_steps_sql = [
    "Setup the application in a development environment",
    "Navigate to the login page",
    "Enter ' OR '1'='1 in the password field and submit",
    "Observe unauthorized access due to the SQL injection"
]

# Step 6: Provide Proof-of-Concept (PoC)
poc_code_sql = """
// Vulnerable Code
String query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'";
Statement stmt = connection.createStatement();
ResultSet rs = stmt.executeQuery(query);
"""

# Step 7: Describe the Impact
impact_sql = "Personal data disclosure and unauthorized access due to bypassed authentication mechanisms."

# Required Changes
fixed_code_sql = """
// Fixed Code
String query = "SELECT * FROM users WHERE username = ? AND password = ?";
PreparedStatement pstmt = connection.prepareStatement(query);
pstmt.setString(1, username);
pstmt.setString(2, password);
ResultSet rs = pstmt.executeQuery();
"""

# XSS Example
issue_type_xss = "Cross-Site Scripting (XSS)"
source_file_xss = "/src/main/webapp/pages/profile.jsp"
commit_xss = "def456gh"
special_config_xss = None
reproduction_steps_xss = [
    "Setup the application and login",
    "Navigate to the profile page",
    "Input <script>alert('XSS')</script> into the bio field",
    "Observe an alert indicating an XSS issue when viewing the profile"
]

poc_code_xss = """
<!-- Vulnerable Code -->
<div>
    <p>${userBio}</p>
</div>
"""

impact_xss = "Attackers can inject malicious scripts, leading to data theft, session hijacking, or defacement."

fixed_code_xss = """
<!-- Fixed Code -->
<div>
    <p>${fn:escapeXml(userBio)}</p>
</div>
"""

# Print Detailed Guide
print("### Steps to Address Code Issues: A Detailed Guide\n")

print("#### SQL Injection")
print(f"**Type of Issue**: {issue_type}")
print(f"**Source File**: {source_file_sql_injection}")
print(f"**Location**: Main branch, commit `{commit}`")
print(f"**Special Configuration**: {special_config_sql}")
print(f"**Reproduction Steps**:")
for step in reproduction_steps_sql:
    print(f"1. {step}")

print("**PoC Code**:")
print(poc_code_sql)

print("**Impact**:")
print(impact_sql)

print("**Required Changes**")
print(fixed_code_sql)

print("\n#### XSS Vulnerability and Fix")
print(f"**Type of Issue**: {issue_type_xss}")
print(f"**Source File**: {source_file_xss}")
print(f"**Location**: Main branch, commit `{commit_xss}`")
print(f"**Special Configuration**: {special_config_xss}")
print(f"**Reproduction Steps**:")
for step in reproduction_steps_xss:
    print(f"1. {step}")

print("**PoC Code**:")
print(poc_code_xss)

print("**Impact**:")
print(impact_xss)

print("**Required Changes**")
print(fixed_code_xss)
```