# Equality Works

## Introduction
Equality Works is a project made by collaboration of 5 coders for a Hackathon organized by Code Institute and sponsored by Deloitte and Trust in SODA. The theme of this Hackathon is based around the gender gap between women in IT sector. Competitors were asked to provide a solution to this problem. 

Equality Works main goal is to provide women as well as other minorities a place where they can easily find jobs which would suit their current needs during various stages of life. While doing our research we have found that one of key issues related to gender gap in IT is retention.  

Many women study hard, get degrees and training to find a job they are not happy in and decide to quit. Our portal provides them with a space where they can find a job that suits their needs, whether it be childcare during after work meetings, inclusive interview panels or mentoring programs they can find the right job here. 

Equality Works gives employers a chance to show off their inclusive policies and find dedicated and happy employees, so it is really a win-win for all parties involved!  

<br>

Screenshot of home page

[Visit the live website on Heroku here](-)



<br>

## Table of Contents


  * [Introduction](#introduction)
  * [UX](#ux)
    + [Strategy](#strategy)
      - [User Stories](#user-stories)
      - [Agile Management](#agile-management)
    + [Scope](#scope)
    + [Structure](#structure)
      - [Design Structure - Site layout](#design-structure---site-layout)
      - [Information Structure - Database Models](#information-structure---database-models)
    + [Skeleton](#skeleton)
      - [Wireframes](#wireframes)
    + [Surface](#surface)
  * [Features](#features)
  * [Future Features](#future-features)
  * [Technologies Used](#technologies-used)
  * [Testing](#testing)
  * [Notable Bugs](#notable-bugs)
  * [SEO](#seo)
- [Deployment](#deployment)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)

## UX

### Strategy

* Site Goals
    * To enable users search for jobs.
    * To allow users add jobs.
    * To have a modern and eye-pleasing design.  
    * To allow users apply to jobs.
    * To improve equality in the workplace  
    * To keep women in IT jobs and improve retention  

* User Goals
    * The ideal employee would be a woman  or a person from a minority who is looking for an inclusive place to work at in IT field.
    * The ideal employer is one that wants to find dedicated workers and is happy to include minorities and close the gender gap.  



#### User Stories
### Some of user stories that got completed 

| #           | User Story      
| ----------- | ------------- 
| 1           | As an employee I want to be able to easily find inclusive jobs with the click of a button. 
| 2           | As an employee I want to be able to delete my account.   
| 3           | As an employee I want to be able to log in and create a profile to save jobs to my account. 
| 4           | As an employee I want to be able to have multiple inclusive categories to find one that suits my needs.    
| 5           | As an employee I want to be able search for jobs by a certain keyword.
| 6           | As an employee I want to have an easy to navigate website on mobile and desktop. 
| 7           | As an employee I want to be able to apply to a job with the click of a button. pixels           
| 8           | As an employee I want to be able to change my email. 
| 9           | As an employee I want to be able to see what some of the job's titles mean.     
| 10          | As an employer I want to be able to add jobs with relevant information like refence number or salary. 
| 11          | As an employer I want to be able to able to delete posted job ads. 
| 12          | As an employer I want to save job ads to view them later.
| 13          | As an employer I want to be able to add relevant inclusivity badges to my job posting. 
| 14          | As an employer I want to delete my account along with all job postings. 

<br/>
<br/>


Some of user stories are planned for next sprint

| #           | User Story      
| ----------- | ------------- 
| 1           | As an employee I want to be able to add profile pictures so potential employers can see how I look like. 
| 2           | As an employer I want to be able to add company logo to my job posts. 
| 3           | As an employer I want to have access to information about how many people saved my job post. 
| 4           | As an employer I want to be able to view potential employees CV with one click. 

<br/>
<br/>


#### Agile Management

Throughout our project we have used Kanban board created in GitHub.  

[Have a look at our Kanban borad](https://github.com/users/asiask97/projects/1/views/1)


We have divided our board into 4 sections.  

We treated each day as an individual sprint. As with usual sprints at the end of each we have planned to have all tasks that were assigned to each person completed.  

Every day we had a stand up meetings where we looked at what was done, what issues were encountered and solutions to any problems 

1. **Done** – this is where all the tasks which were completed went. Throughout the project we could all see this section fill up, which motivated us even more.  
2. **In Process** - this section included all the things we were currently working on. We picked out the most important tasks and assigned them to one or two people based on their abilities and interests. 
3. **Todo** – here we placed the most important things from the backlog. We always wanted to have something in this section to avoid any down time where someone does not know what they should do. 
4. **Backlog** – The backlog contained all the user stories and functions that we wanted to include in our project. Items were taken from backlog based on their priority. 

Here you can see our Kanban board mid sprint 
![Kanban board mid sprit](/static/documentation/kanban.png)




### Scope
After having analyzed user stories as a team we have developed a high-level view of what our project should contain and how it should be structured to be the most efficient and easy to navigate. We have decided on the fallowing technical features: 

- Calculator – can compare their future income to their current salary 
- Jobs – jobs can be added by employers 
- Saving – jobs can be saved by any user 
- Register – user can create an account as employee or employer 
- Login – user can login to view saved jobs 
- Deletion – user can delete account and update information. Job posts can be deleted 

### Structure

#### Design Structure - Site layout
* The design of this website should be clear and intuitive. There should be a navigation bar at the top for easy navigation and ‘hamburger’ navigation bar on mobile phones.  
* All navigation and buttons should be in highly visible places. 
* All forms should be simple and easy to fill out.  

#### Information Structure - Database Models

After a team meeting, we decided on a relational database. Our database system consists of 3 tables.  

- The Users table contains all the credentials necessary for a user's account. Each user when registering is asked to choose whether they are an employee or employer this is saved in ‘userType’ field.  

- The Jobs table has all the details needed for a job posting. Each job has a ‘created_by’ field with a foreign key that helps to identify the user who created this job post. Each user can have multiple job posts, so this is one to many relationship. All the fields with Boolean type are badges used to identify the inclusivity that the employer is providing. On creation of the job the employer chooses the relevant fields, and those fields will hold the value of ‘True’. This helps to search for jobs by their badges.  

- The Savedjobs table helps to identify all the saved jobs by the user. It consists of primary key field that helps to identify the savejobs item and two foreign keys, one has many to many relationships with the Users table to have access to the correct user and the other has many to many relationship with Jobs table to help identify which job was saved. This combination gets us the lists of jobs that the user has saved.  

![databse shema](/static/documentation/database.png)

 

<img of databse shema> 

### Skeleton

#### Wireframes

All wireframes were designed base on mobile first principle, along side with a tablet and destop view. You can see all wireframes [here](static/documentation/wireframes.md).

### Surface

* Fonts - 


* Images - 


* Colours - 




## Features
 Equality works has many useful and interesting features which will help reduce or even eliminate the gender gap in IT. The gender gap starts off with many workplaces being not inclusive enough to women and other minorities in IT. Equality Works is a job posting platform which helps to reduce the gender gap by promoting inclusive working environments. We are hoping that employees will be encouraged by badges to become a more attractive workplace for all and gain higher visibility on the platform as the users are encouraged to search by badge type which suits their current needs. 

### Employee Features


#### **Homepage**
Equality Works home page has a modern and flesh look. Every bit of text is easily readable and the slide in animations adds in some interaction as the user explores the page.  

- The first thing the user sees is a hero image and brief explanation of what this website does.  

- Further down user is introduced to concept of badges. If a badge interests the user, it may be clicked. The user will be taken to a search with displays all the jobs from the database where the employers who included this badge in their job post.  

- Below the list of badges, the user can find a calculator where they can calculate how much more they might gain if they decide to switch to id. This was included to motivate women to change jobs into IT, hence reduction the gender gap.  

- At the bottom of the home page the user can find more information on why this project was created and how we are planning to help women and minorities reduce the gender gap. 
screenshot here

====================================== ADD SCRENSHOTS OF EACH SECTION  =========================================
#### **Jobs**  
The job listings page is the essence of Equality Works. 

- On this subpage of the website, we can see all the jobs that were added by employers. Those jobs can be filtered by badges at the top of the page or if user clicks on the badge on job listing itself. This is a very intuitive and effortless way to filter jobs. The more badges a job post has the better because it will appear in more searches, this motivates the employer to be more inclusive and helps employee to find inclusive jobs.  

- The user can click on the save button if they are logged in which will save the jobs for later use. 

- The job description is hidden until the user chooses to learn more about the job by clicking ‘View Detail’ button. 

- Apply now! Button lets user apply to a job with just one single click! 
screenshot here

#### **Resources**  


#### **Create new job listing**


#### **Mentors**


#### **Support Pages**
* Login

  Img here
* Register 

  Img here
* Profile

  Img here

## Future Features

There are a number of features which the team plans to implement in the future. They were left out due to constraints in terms of time and scope, but are indicative of the future direction of the site and the ways in which it could expand.
* Image Uploading - this feature would allow users to upload images to use as a profile picture and companies to upload images for use as their logo.
* Document Management - since user profiles have already been created on the site, by allowing the uploading and storing of CV’s, cover letters etc, these can then be attached to any job application made through the site automatically, saving the user time and effort.
* Multiple Criteria Filtering - currently the site filters jobs based on a single criteria at a time, in the future this could be expanded to filter on multiple fields at once.
* Social Media Integration - for users, social media sign-in could be integrated, allowing the use of a Google or Facebook account to log in to the site. Social media share buttons could be added to job posts to allow easy sharing, and with the use of the Twitter API new job posts could be automatically posted to social media channels.
* Application Management - Since we have profiles for both employees and employers, we could also build functionality to manage the creation and tracking of job applications, providing a central admin interface for employers to screen and select interview candidates.
* Issues Tackled - the site is focussed on tackling a number of important issues which affect the gender balance of jobs in tech. After the site has been in use and user feedback has been collected, these topics could be refined and expanded upon.


## Search Engine Optimization

Description of meta-tags and any keyword research





## Technologies Used

* Python
    * These Python modules were used for the project:
      ```
      click==8.1.3
      Flask==2.2.2
      Flask-Cors==3.0.10
      Flask-Login==0.6.2
      flask-marshmallow==0.14.0
      Flask-SQLAlchemy==2.5.1
      greenlet==1.1.3
      gunicorn==20.1.0
      importlib-metadata==4.12.0
      itsdangerous==2.1.2
      Jinja2==3.1.2
      MarkupSafe==2.1.1
      marshmallow==3.17.1
      marshmallow-sqlalchemy==0.28.1
      packaging==21.3
      psycopg2-binary==2.9.3
      pyparsing==3.0.9
      six==1.16.0
      SQLAlchemy==1.4.40
      Werkzeug==2.2.2
      WTForms==3.0.1
      zipp==3.8.1
      ```

* Heroku
    * The project was deployed using Heroku's cloud-based platform
* Heroku PostgreSQL
    * description
* HTML
    * description
* CSS
    * description
* Bootstrap
    * description
* Font Awesome
    * description


#### Other Resources Used
* [Github](https://github.com) 
    * GitHub is used for version control and as a repository for the code of the project.
* [Gitpod](https://gitpod.io) 
    * Gitpod was the development environment for this site and linked to Github for storage and deployment.



## Testing

User testing described here


## Notable Bugs

Any outstanding bugs here


# Deployment

## Creating the Project
1. A new repository was created for the project on GitHub by clicking 'New Repository' on the GitHub user page, giving a name to the project.
1. The GitPod link created by the Chrome extension was clicked on the Code Institute Python template found [here](https://github.com/Code-Institute-Org/python-essentials-template).
1. This created a virtual workspace which was then linked to my GitHub account.
1. After writing code for the project, I used git commands add, commit and push which sent all the project files from GitPod to my GitHub repository.

## Deploying to Heroku
The project was deployed on the Heroku site by using these steps:
1. Create a new account on Heroku.
1. Log into your account.
1. Click on the 'New' button and click 'Create New App'.
1. Choose a new name for your app, which must be globally unique to your app.
1. Select the Resources menu option from the top of the page.
1. Search in the Add-ons search box for Heroku Postgres.
1. Select the Heroku Postgres Add on from the results list and accept the hobby level tier.
1. Click on the settings tab and go to the hidden variables section.
1. Here you can add your SECRET_KEY variable which is hidden within the env.py in your Django project. It is a good idea to generate a new secret key rather than using the default one.
1. Make a note of the DATABASE_URL so that you can use it in your own env.py to connect directly to the Heroku databse during development.
1. You can also add a key for static storage such as Cloudinary or S3.
1. Click the Deploy tab in Heroku.
1. Connect your project to your Github Repository and select automatic deployment. This will deploy your project after every time you push your changes to Github.
1. For an e-commerce project such as this, you will need to use Stripe or another payment provider. 
1. Once you sign up with a payment provider, add their API keys to the secret variables section on Heroku and in your own env.py file.


## Local Deployment

#### Forking the repo on GitHub
1. Navigate to the Github page and log into your GitHub account.
1. Navigate to the project page
1. Click on the 'Fork' icon on the upper right hand side of the screen.
1. This makes a copy of the code in your own repo so you can examine it or open it in an IDE.



# Credits

## Code

## Data

## Pictures

* Taken from ...


## Coding Inspiration

[Youtube - codemy.com](https://www.youtube.com/watch?v=0Qxtt4veJIc&list=PLCC34OHNcOtolz2Vd9ZSeSXWc8Bq23yEz&ab_channel=Codemy.com) - Walk through building a simple blog. <br>




# Acknowledgements

* 
