from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

s = Service('/usr/bin/geckodriver')
driver = webdriver.Firefox(service=s)

driver.get('http://15.206.145.37:8080/')

driver.implicitly_wait(3)

driver.find_element(By.ID, 'j_username').send_keys('cicdation')
driver.find_element(By.NAME, 'j_password').send_keys('KIIT2024')
driver.find_element(By.NAME, 'Submit').click()

driver.implicitly_wait(3)

driver.find_element(By.XPATH, "//a[@href='/view/all/newJob']").click()

driver.implicitly_wait(3)

job_name = input('Enter the job name:- ')
driver.find_element(By.ID, 'name').send_keys(job_name)

print("1. Freestyle Project")
print("2. Pipeline")
print("3. Multi-configuration  Project")
print("4. Folder")
print("5. Multibranch Pipeline")
print("6. Organization Folder")

job_type = int(input('Enter the job type(Enter the Sr.No.):- '))
while job_type < 1 or job_type > 6:
    print("Please enter the job number correctly!")
    job_type = int(input('Enter the job type(Enter the Sr.No.):- '))

match job_type:
    case 1:
        driver.find_element(
            By.XPATH, "//li[@class='hudson_model_FreeStyleProject']//label").click()
    case 2:
        driver.find_element(
            By.XPATH, "// div[@id='j-add-item-type-standalone-projects']//li[1]//div[1]").click()
    case 3:
        driver.find_element(
            By.XPATH, "//li[@class='hudson_matrix_MatrixProject']//label").click()
    case 4:
        driver.find_element(
            By.XPATH, "//li[@class='com_cloudbees_hudson_plugins_folder_Folder']//label").click()
    case 5:
        driver.find_element(
            By.XPATH, "//li[@class='org_jenkinsci_plugins_workflow_multibranch_WorkflowMultiBranchProject']//label").click()
    case 6:
        driver.find_element(
            By.XPATH, "//li[@class='jenkins_branch_OrganizationFolder']//label").click()
    case default:
        print("Error! No such option exist!")
        quit()

driver.find_element(By.ID, 'ok-button').click()

driver.implicitly_wait(3)

if job_type == 1:
    desc = input('Enter the description:- ')
    driver.find_element(By.NAME, 'description').send_keys(desc)
    while True:
        print("1. Discard old builds.")
        print("2. Github Project.")
        print("3. This project is parameterized.")
        print("4. Throttle builds.")
        print("5. Execute concurrent builds if necessary.")
        print("6. Done selecting.")
        option = int(input('Enter the option(Enter the Sr.No.):- '))
        match option:
            case 1:
                check = driver.find_element(
                    By.XPATH, "//label[normalize-space()='Discard old builds']")
                driver.execute_script("arguments[0].click();", check)
            case 2:
                check = driver.find_element(
                    By.XPATH, "//label[normalize-space()='GitHub project']")
                driver.execute_script("arguments[0].click();", check)
            case 3:
                check = driver.find_element(
                    By.XPATH, "//label[normalize-space()='This project is parameterized']")
                driver.execute_script("arguments[0].click();", check)
            case 4:
                check = driver.find_element(
                    By.XPATH, "//label[normalize-space()='Throttle builds']")
                driver.execute_script("arguments[0].click();", check)
            case 5:
                check = driver.find_element(
                    By.XPATH, "//label[normalize-space()='Execute concurrent builds if necessary']")
                driver.execute_script("arguments[0].click();", check)
            case 6:
                print("OK! Done selecting.")
                break
            case default:
                print("Error! No such option exist!")
                quit()

    attach_git_repo = input("Do you want to add a git repository url? (Y/N)")
    if attach_git_repo == 'Y' or attach_git_repo == 'y':
        git = driver.find_element(By.XPATH, "//label[@for='radio-block-1']")
        driver.execute_script("arguments[0].click();", git)
        url = input('Enter the url of your git repository:- ')
        driver.find_element(By.NAME, '_.url').send_keys(url)

    while True:
        print("1. Trigger builds remotely (e.g., from scripts).")
        print("2. Build after other projects are built.")
        print("3. Build periodically.")
        print("4. GitHub hook trigger for GITScm polling.")
        print("5. Poll SCM.")
        print("6. Done selecting.")
        option = int(input('Enter the option(Enter the Sr.No.):- '))
        match option:
            case 1:
                check = driver.find_element(
                    By.XPATH, "//label[normalize-space()='Trigger builds remotely (e.g., from scripts)']")
                driver.execute_script("arguments[0].click();", check)
            case 2:
                check = driver.find_element(
                    By.XPATH, "//label[normalize-space()='Build after other projects are built']")
                driver.execute_script("arguments[0].click();", check)
            case 3:
                check = driver.find_element(
                    By.XPATH, "//label[normalize-space()='Build periodically']")
                driver.execute_script("arguments[0].click();", check)
            case 4:
                check = driver.find_element(
                    By.XPATH, "//label[normalize-space()='GitHub hook trigger for GITScm polling']")
                driver.execute_script("arguments[0].click();", check)
            case 5:
                check = driver.find_element(
                    By.XPATH, "//label[normalize-space()='Poll SCM']")
                driver.execute_script("arguments[0].click();", check)
            case 6:
                print("OK! Done selecting.")
                break
            case default:
                print("Error! No such option exist!")
                quit()

    while True:
        print("1. Delete workspace before build starts.")
        print("2. Use secret text(s) or file(s).")
        print("3. Add timestamps to the Console Output.")
        print("4. Inspect build log for published build scans.")
        print("5. Terminate a build if it's stuck.")
        print("6. With Ant.")
        print("7. Done Selecting.")
        option = int(input('Enter the option(Enter the Sr.No.):- '))
        match option:
            case 1:
                check = driver.find_element(
                    By.XPATH, "//label[normalize-space()='Delete workspace before build starts']")
                driver.execute_script("arguments[0].click();", check)
            case 2:
                check = driver.find_element(
                    By.XPATH, "//label[normalize-space()='Use secret text(s) or file(s)']")
                driver.execute_script("arguments[0].click();", check)
            case 3:
                check = driver.find_element(
                    By.XPATH, "//label[normalize-space()='Add timestamps to the Console Output']")
                driver.execute_script("arguments[0].click();", check)
            case 4:
                check = driver.find_element(
                    By.XPATH, "//label[normalize-space()='Inspect build log for published build scans']")
                driver.execute_script("arguments[0].click();", check)
            case 5:
                check = driver.find_element(
                    By.XPATH, "//label[normalize-space()='Terminate a build if it's stuck']")
                driver.execute_script("arguments[0].click();", check)
            case 6:
                check = driver.find_element(
                    By.XPATH, "//label[normalize-space()='With Ant']")
                driver.execute_script("arguments[0].click();", check)
            case 7:
                print("OK! Done selecting.")
                break
            case default:
                print("Error! No such option exist!")
                quit()
    driver.find_element(By.ID, 'yui-gen23-button').click()
    print("Job created successfully!")

elif job_type == 2:
    desc = input('Enter the description:- ')
    driver.find_element(By.NAME, 'description').send_keys(desc)
    while True:
        print("1. Discard old builds.")
        print("2. Do not allow concurrent builds.")
        print("3. Do not allow the pipeline to resume if the controller restarts.")
        print("4. GitHub project.")
        print("5. Pipeline speed/durability override.")
        print("6. Preserve stashes from completed builds.")
        print("7. This project is parameterized.")
        print("8. Throttle builds.")
        print("9. Done Selecting.")
        option = int(input('Enter the option(Enter the Sr.No.):- '))
        match option:
            case 1:
                check = driver.find_element(
                    By.XPATH, "//label[normalize-space()='Discard old builds']")
                driver.execute_script("arguments[0].click();", check)
            case 2:
                check = driver.find_element(
                    By.XPATH, "//label[normalize-space()='Do not allow concurrent builds']")
                driver.execute_script("arguments[0].click();", check)
            case 3:
                check = driver.find_element(
                    By.XPATH, "// label[contains(text(), 'Do not allow the pipeline to resume if the control')]")
                driver.execute_script("arguments[0].click();", check)
            case 4:
                check = driver.find_element(
                    By.XPATH, "//label[normalize-space()='GitHub project']")
                driver.execute_script("arguments[0].click();", check)
            case 5:
                check = driver.find_element(
                    By.XPATH, "//label[normalize-space()='Pipeline speed/durability override']")
                driver.execute_script("arguments[0].click();", check)
            case 6:
                check = driver.find_element(
                    By.XPATH, "//label[normalize-space()='Preserve stashes from completed builds']")
                driver.execute_script("arguments[0].click();", check)
            case 7:
                check = driver.find_element(
                    By.XPATH, "//label[normalize-space()='This project is parameterized']")
                driver.execute_script("arguments[0].click();", check)
            case 8:
                check = driver.find_element(
                    By.XPATH, "//label[normalize-space()='Throttle builds']")
                driver.execute_script("arguments[0].click();", check)
            case 9:
                print("OK! Done selecting.")
                break
            case default:
                print("Error! No such option exist!")
                quit()

    while True:
        print("1. Build after other projects are built.")
        print("2. Build periodically.")
        print("3. GitHub hook trigger for GITScm polling.")
        print("4. Poll SCM.")
        print("5. Quiet period.")
        print("6. Trigger builds remotely (e.g., from scripts).")
        print("7. Done Selecting.")
        option = int(input('Enter the option(Enter the Sr.No.):- '))
        match option:
            case 1:
                check = driver.find_element(
                    By.XPATH, "//label[normalize-space()='Build after other projects are built']")
                driver.execute_script("arguments[0].click();", check)
            case 2:
                check = driver.find_element(
                    By.XPATH, "//label[normalize-space()='Build periodically']")
                driver.execute_script("arguments[0].click();", check)
            case 3:
                check = driver.find_element(
                    By.XPATH, "//label[normalize-space()='GitHub hook trigger for GITScm polling']")
                driver.execute_script("arguments[0].click();", check)
            case 4:
                check = driver.find_element(
                    By.XPATH, "// label[normalize-space()='Poll SCM']")
                driver.execute_script("arguments[0].click();", check)
            case 5:
                check = driver.find_element(
                    By.XPATH, "//label[normalize-space()='Quiet period']")
                driver.execute_script("arguments[0].click();", check)
            case 6:
                check = driver.find_element(
                    By.XPATH, "//label[normalize-space()='Trigger builds remotely (e.g., from scripts)']")
                driver.execute_script("arguments[0].click();", check)
            case 7:
                print("OK! Done selecting.")
                break
            case default:
                print("Error! No such option exist!")
                quit()
    driver.find_element(By.XPATH, "//button[@id='yui-gen4-button']").click()
    display_name = input('Enter the display name:- ')
    driver.find_element(
        By.XPATH, "//input[@name='_.displayNameOrNull']").send_keys(display_name)
    script = input('Enter the script:- ')
    driver.find_element(
        By.XPATH, "//textarea[@role='textbox']").send_keys(script)
    driver.find_element(By.ID, 'yui-gen6-button').click()
    print("Job created successfully!")

elif job_type == 3:
    desc = input('Enter the description:- ')
    driver.find_element(By.NAME, 'description').send_keys(desc)
    while True:
        print("1. Discard old builds.")
        print("2. GitHub project.")
        print("3. This project is parameterized.")
        print("4. Throttle builds.")
        print("5. Execute concurrent builds if necessary.")
        print("6. Done Selecting.")
        option = int(input('Enter the option(Enter the Sr.No.):- '))
        match option:
            case 1:
                check = driver.find_element(
                    By.XPATH, "//label[normalize-space()='Discard old builds']")
                driver.execute_script("arguments[0].click();", check)
            case 2:
                check = driver.find_element(
                    By.XPATH, "//label[normalize-space()='GitHub project']")
                driver.execute_script("arguments[0].click();", check)
            case 3:
                check = driver.find_element(
                    By.XPATH, "//label[normalize-space()='This project is parameterized']")
                driver.execute_script("arguments[0].click();", check)
            case 4:
                check = driver.find_element(
                    By.XPATH, "//label[normalize-space()='Throttle builds']")
                driver.execute_script("arguments[0].click();", check)
            case 5:
                check = driver.find_element(
                    By.XPATH, "//label[normalize-space()='Execute concurrent builds if necessary']")
                driver.execute_script("arguments[0].click();", check)
            case 6:
                print("OK! Done selecting.")
                break
            case default:
                print("Error! No such option exist!")
                quit()
    advanced = input("Do you want to add advanced options? (Y/N):- ")
    if advanced == 'Y' or advanced == 'y':
        driver.find_element(
            By.XPATH, "//button[@id='yui-gen18-button']").click()
        while True:
            print("1. Quiet Period.")
            print("2. Retry Count.")
            print("3. Block build when upstream project is building.")
            print("4. Block build when downstream project is building")
            print("5. Use custom workspace.")
            print("6. Use custom child workspace.")
            print("7. Done selecting.")
            option = int(input('Enter the option(Enter the Sr.No.):- '))
            match option:
                case 1:
                    check = driver.find_element(
                        By.XPATH, "//label[normalize-space()='Quiet period']")
                    driver.execute_script("arguments[0].click();", check)
                case 2:
                    check = driver.find_element(
                        By.XPATH, "//label[normalize-space()='Retry Count']")
                    driver.execute_script("arguments[0].click();", check)
                case 3:
                    check = driver.find_element(
                        By.XPATH, "//label[normalize-space()='Block build when upstream project is building']")
                    driver.execute_script("arguments[0].click();", check)
                case 4:
                    check = driver.find_element(
                        By.XPATH, "//label[normalize-space()='Block build when downstream project is building']")
                    driver.execute_script("arguments[0].click();", check)
                case 5:
                    check = driver.find_element(
                        By.XPATH, "//label[normalize-space()='Use custom workspace']")
                    driver.execute_script("arguments[0].click();", check)
                case 6:
                    check = driver.find_element(
                        By.XPATH, "//label[normalize-space()='Use custom child workspace']")
                    driver.execute_script("arguments[0].click();", check)
                case 7:
                    print("OK! Done selecting.")
                    break
                case default:
                    print("Error! No such option exist!")
                    quit()
        display_name = input('Enter the display name:- ')
        driver.find_element(
            By.XPATH, "//input[@name='_.displayNameOrNull']").send_keys(display_name)
        attach_git_repo = input(
            "Do you want to add a git repository url? (Y/N)")
    if attach_git_repo == 'Y' or attach_git_repo == 'y':
        git = driver.find_element(By.XPATH, "//label[@for='radio-block-1']")
        driver.execute_script("arguments[0].click();", git)
        url = input('Enter the url of your git repository:- ')
        driver.find_element(By.NAME, '_.url').send_keys(url)

    while True:
        print("1. Trigger builds remotely (e.g., from scripts).")
        print("2. Build after other projects are built.")
        print("3. Build periodically.")
        print("4. GitHub hook trigger for GITScm polling.")
        print("5. Poll SCM.")
        print("6. Done Selecting.")
        option = int(input('Enter the option(Enter the Sr.No.):- '))
        match option:
            case 1:
                check = driver.find_element(
                    By.XPATH, "//label[normalize-space()='Trigger builds remotely (e.g., from scripts)']")
                driver.execute_script("arguments[0].click();", check)
            case 2:
                check = driver.find_element(
                    By.XPATH, "//label[normalize-space()='Build after other projects are built']")
                driver.execute_script("arguments[0].click();", check)
            case 3:
                check = driver.find_element(
                    By.XPATH, "//label[normalize-space()='Build periodically']")
                driver.execute_script("arguments[0].click();", check)
            case 4:
                check = driver.find_element(
                    By.XPATH, "//label[normalize-space()='GitHub hook trigger for GITScm polling']")
                driver.execute_script("arguments[0].click();", check)
            case 5:
                check = driver.find_element(
                    By.XPATH, "//label[normalize-space()='Poll SCM']")
                driver.execute_script("arguments[0].click();", check)
            case 6:
                print("OK! Done selecting.")
                break
            case default:
                print("Error! No such option exist!")
                quit()

    while True:
        print("1. Combination Filter.")
        print("2. Run each configuration sequentially.")
        print("3. Execute touchstone builds first.")
        print("4. Done Selecting.")
        option = int(input('Enter the option(Enter the Sr.No.):- '))
        match option:
            case 1:
                check = driver.find_element(
                    By.XPATH, "//label[normalize-space()='Combination Filter']")
                driver.execute_script("arguments[0].click();", check)
            case 2:
                check = driver.find_element(
                    By.XPATH, "//label[normalize-space()='Run each configuration sequentially']")
                driver.execute_script("arguments[0].click();", check)
            case 3:
                check = driver.find_element(
                    By.XPATH, "//label[normalize-space()='Execute touchstone builds first']")
                driver.execute_script("arguments[0].click();", check)
            case 4:
                print("OK! Done selecting.")
                break
            case default:
                print("Error! No such option exist!")
                quit()

    while True:
        print("1. Delete workspace before build starts.")
        print("2. Use secret text(s) or file(s).")
        print("3. Add timestamps to the Console Output.")
        print("4. Inspect build log for published build scans.")
        print("5. Terminate a build if it's stuck.")
        print("6. With Ant.")
        print("7. Done selecting.")
        option = int(input('Enter the option(Enter the Sr.No.):- '))
        match option:
            case 1:
                check = driver.find_element(
                    By.XPATH, "//label[normalize-space()='Delete workspace before build starts']")
                driver.execute_script("arguments[0].click();", check)
            case 2:
                check = driver.find_element(
                    By.XPATH, "//label[normalize-space()='Use secret text(s) or file(s)']")
                driver.execute_script("arguments[0].click();", check)
            case 3:
                check = driver.find_element(
                    By.XPATH, "//label[normalize-space()='Add timestamps to the Console Output']")
                driver.execute_script("arguments[0].click();", check)
            case 4:
                check = driver.find_element(
                    By.XPATH, "//label[normalize-space()='Inspect build log for published build scans']")
                driver.execute_script("arguments[0].click();", check)
            case 5:
                check = driver.find_element(
                    By.XPATH, "//label[normalize-space()='Terminate a build if it's stuck']")
                driver.execute_script("arguments[0].click();", check)
            case 6:
                check = driver.find_element(
                    By.XPATH, "//label[normalize-space()='With Ant']")
                driver.execute_script("arguments[0].click();", check)
            case 7:
                print("OK! Done selecting.")
                break
            case default:
                print("Error! No such option exist!")
                quit()
    driver.find_element(By.ID, 'yui-gen25-button').click()
    print("Job created successfully!")

elif job_type == 4:
    display_name = input('Enter the display name:- ')
    driver.find_element(
        By.XPATH, "//input[@name='_.displayNameOrNull']").send_keys(display_name)
    desc = input('Enter the description:- ')
    driver.find_element(By.NAME, '_.description').send_keys(desc)
    driver.find_element(By.ID, 'yui-gen6-button').click()
    print('Job created successfully!')

elif job_type == 5:
    display_name = input('Enter the display name:- ')
    driver.find_element(
        By.XPATH, "//input[@name='_.displayNameOrNull']").send_keys(display_name)
    desc = input('Enter the description:- ')
    driver.find_element(By.NAME, '_.description').send_keys(desc)
    print('1. Git')
    print('2. Github')
    print('3. Single repository & branch')
    source = driver.find_element(By.ID, 'yui-gen1-button')
    for option in source.find_elements(By.TAG_NAME, 'option'):
        if option.text == 'Git':
            option.click()
            project_repo = input('Enter the project repo link :- ')
            driver.find_element(By.NAME, '_.remote').send_keys(project_repo)
            break
        elif option.text == 'Github':
            option.click()
            project_repo = input('Enter the project repo link :- ')
            driver.find_element(
                By.NAME, '_.repositoryUrl').send_keys(project_repo)
            break
        elif option.text == 'Single repository & branch':
            option.click()
            name = input('Enter the name :- ')
            driver.find_element(By.NAME, '_.name').send_keys(name)
            git_url = input('Enter the repository url :-')
            driver.find_element(By.NAME, '_.url').send_keys(git_url)
            break
    driver.find_element(By.ID, 'yui-gen8-button').click()
    print('Job created successfully!')

elif job_type == 6:
    display_name = input('Enter the display name:-')
    driver.find_element(
        By.XPATH, "//input[@name='_.displayNameOrNull']").send_keys(display_name)
    desc = input('Enter the description:-')
    driver.find_element(By.NAME, '_.description').send_keys(desc)
    driver.find_element(By.ID, 'yui-gen15-button').click()
    print('Job created successfully!')

print('Program execution completed successfully!!')
