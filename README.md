The Alumni Management System is a dynamic web application designed to connect and engage alumni by providing a digital platform where they can interact, share updates, and collaborate. This platform facilitates an alumni directory, event scheduling, and a newsfeed for announcements, enhancing the community engagement among graduates. Additionally, it supports user authentication and encryption of user credentials. With collaboration features, it allows alumni to connect for various opportunities and initiatives. The application is built using Flask for the webapp, PostgreSQL for data management, and employs modern HTML, CSS, and JavaScript for the frontend, ensuring a seamless and interactive user experience. Deployed on Render, it leverages powerful server-client architecture for a robust deployment.

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
            (photo gallery)

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