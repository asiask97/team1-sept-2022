# Equality Works

## Introduction


Intro goes here

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
    * To enable users search for jobs

* User Goals



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



### Structure

#### Design Structure - Site layout
* 

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

### Employer Features

#### * Create new job listing
Description






## Future Features

List of outstanding features for future development 


## Search Engine Optimization

Description of meta-tags and any keyword research





## Technologies Used

* Python
    * These Python modules were used for the project:
       * Paste modules from requirements.txt


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

[Google](https://www.google.ie/) - code credits here <br>


# Acknowledgements

* 
