# ASRJC Alumni Portal

## Inspiration
The ASRJC Alumni Portal was inspired by the rich heritage of Anderson Serangoon Junior College and its predecessor institutions, Anderson Junior College and Serangoon Junior College. With histories dating back to 1984, these institutions have fostered a large community of alumni. This portal aims to harness this vibrant history to inspire current students and alumni, encouraging them to reach new heights of success and to foster a tightly-knit community.

## What it does
The ASRJC Alumni Portal serves as a dynamic platform designed to engage alumni by facilitating connections and collaborations. It offers an alumni directory, event scheduling functionalities, collaboration between alumnis and a newsfeed for announcements. It also includes robust features such as user authentication and secure handling of credentials, making it a comprehensive tool for community engagement.

## How it's built
The application leverages Flask as its backend framework, with PostgreSQL handling data management tasks. The frontend is crafted using modern HTML, CSS, and JavaScript, ensuring a responsive and interactive user experience. Deployed on Render, the platform benefits from a reliable server-client architecture that supports scalable web applications.

## Challenges encountered
Throughout the development process, numerous challenges were encountered:
- **Frontend Integration:** Bridging HTML, CSS, and JavaScript posed a steep learning curve, with significant time invested in debugging and achieving functional synergies between the technologies.
- **Backend Complexity:** Configuring the PostgreSQL database and integrating it with Flask required a deep dive into SQL and backend architecture as well as a methodology to populate sample data. 
- **Security and Session Management:** Implementing robust security measures and managing user sessions to safeguard personal information was critical and challenging.
- **Deployment Issues:** Initial deployment attempts on Vercel were hindered by compatibility issues with Flask, leading to a strategic pivot to Render for better support at the eleventh hour.

## Accomplishments that I'm proud of
- **Successful Deployment:** Overcoming deployment challenges and successfully launching the portal on Render was a significant milestone.
- **Practical Application of Skills:** The project was a valuable opportunity to apply theoretical knowledge in a real-world project, seeing the concepts in action.

## What I learned
This project was immensely educational, covering several aspects:
- **Advanced CSS Techniques:** Mastering CSS to enhance the website's aesthetic and user experience and giving a consistent look across pages. 
- **Full-stack Integration:** Understanding the intricate dance between the frontend and backend.
- **Debugging and Tools:** Utilizing local and online debugging tools to resolve issues effectively both on the local server as well as on the online server. These include browser inspeciton tools, server logs and powershell debugs as well as error handling in the code. 
- **JavaScript Dynamics:** Leveraging JavaScript to manage dynamic content and enhance user interaction.

## What's next for ASRJC Alumni Portal
Future enhancements for the portal include:
- **Admin Dashboard:** Introducing an administrative toolkit for managing user accounts, news, and events.
- **Blog and Email Integration:** Incorporating a blogging feature and linking it with an email server to automate notifications for collaboration requests and updates.
- **Enhanced Interactivity:** Implementing more interactive features such as live chats and forums to further boost alumni engagement.


File Directory
app

    static
        style.css

        js

            alumni-directory.js
            auth.js
            carousel.js
            profile.js

        images
            (system images)
        
        gallery
            (website images)

    templates
        alumni-directory.html
        events.html
        index.html
        newsfeed.html
        profile.html
        register-login.html
        gallery.html 

    __init__.py
    config.py
    database.py
    models.py
    pwd_hashing.py
    routes.py
   
requirements.txt
run.py
README.md