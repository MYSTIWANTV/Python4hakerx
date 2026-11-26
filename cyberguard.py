# CyberGuard v1.0 - beginner account security assessment

border = "=" * 44
divider = "-" * 44
critical_limit = 5

print(border)
print("===============CYBERGUARD v1.0===============")
print("    PERSONAL SECURITY MONITORING SYSTEM")
print(border)
print()
print("Welcome, Security Analyst!")
print("Review account information and identify potential threats.")
print("Starting security assessment...")
print()

username = input("Username: ").strip()
email = input("Email address: ").strip()
password = input("Sample password (visible while typing): ")
age_input = input("Age in whole years: ").strip()
ip_address = input("IP address: ").strip()
attempts_input = input("Failed login attempts: ").strip()
status_input = input("Account status (Active or Inactive): ").strip().lower()

# Validate the inputs before converting them.
if not age_input.isdecimal() or not attempts_input.isdecimal():
    print("Age and failed login attempts must be non-negative whole numbers.")
elif status_input != "active" and status_input != "inactive":
    print("Account status must be Active or Inactive.")
else:
    age = int(age_input)
    failed_attempts = int(attempts_input)

    if status_input == "active":
        account_active = True
        account_status = "ACTIVE"
    else:
        account_active = False
        account_status = "INACTIVE"

    # Only the length is needed for the educational password check.
    password_length = len(password)
    del password

    if password_length < 8:
        password_assessment = "WEAK"
    elif password_length < 12:
        password_assessment = "MODERATE"
    else:
        password_assessment = "STRONG"

    if failed_attempts == 0:
        login_alert = "[INFO] No failed login attempts detected."
    elif failed_attempts < critical_limit:
        login_alert = "[LOW] Low security alert."
    else:
        login_alert = "[CRITICAL] Critical warning: Possible brute-force attack."

    # An inactive account can still have suspicious login activity.
    if failed_attempts >= critical_limit:
        threat_level = "HIGH"
        recommendation = "Investigate the login activity and secure the account immediately."
    else:
        threat_level = "LOW"
        if account_active:
            if failed_attempts == 0:
                recommendation = "Continue routine monitoring."
            else:
                recommendation = "Review the failed attempts and monitor for further activity."
        else:
            recommendation = "Keep access disabled and review the recorded login activity."

    # Express the critical threshold as a float for the report.
    threshold_value = float(critical_limit)

    print()
    print(border)
    print("===============CYBERGUARD SECURITY REPORT===============")
    print(border)

    print()
    print("USER INFORMATION")
    print(divider)
    print("Username: " + username)
    print("Email: " + email)
    print("Age: " + str(age))
    print("IP Address: " + ip_address)
    print("Account Status: " + account_status)

    print()
    print("SECURITY ANALYSIS")
    print(divider)
    print("Password Assessment: " + password_assessment)
    print("Failed Login Attempts: " + str(failed_attempts))
    print("Critical Alert Threshold: " + str(threshold_value) + " attempts")
    print("Python data types (age, threshold, active):",
          type(age), type(threshold_value), type(account_active))

    print()
    print("THREAT DETECTION")
    print(divider)
    print(login_alert)
    if not account_active:
        print("[WARNING] Account access is currently disabled.")
    elif failed_attempts < critical_limit:
        print("[INFO] No critical login threat detected.")

    print()
    print("FINAL SECURITY STATUS")
    print(divider)
    print("THREAT LEVEL: " + threat_level)
    print()
    print("RECOMMENDATION")
    print(recommendation)
    if password_assessment == "WEAK":
        print("Choose a longer password.")

    print()
    print(border)
    print("===============END OF SECURITY REPORT===============")
    print(border)
