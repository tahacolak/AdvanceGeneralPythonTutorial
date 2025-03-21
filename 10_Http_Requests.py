'''
@author: tahacolak
Notes from the Author:
   🌐 What is an HTTP Request?:
    HTTP (HyperText Transfer Protocol) is the foundation of data communication on the web.
    An HTTP request is a message sent by a client (usually a web browser or app) to a server to request data or an action.
    When you type a URL into your browser like https://blablabla.com, your browser sends an HTTP request to the server that hosts that site.

    I-) Client sends an HTTP request to the server.
        For example: GET /index.html → asking for the homepage.

    II-) Server receives the request, processes it (maybe checks a database), and creates a response.
         
    III-) Server sends an HTTP response back to the client.
          ! The response might include: 
            *HTML page,
            *JSON data,
            *Image, file, etc.
    IV-)Client receives the response and displays it or uses it accordingly.

    💻 Client-Server Working Mentality:
    From CLIENT-Side("The Requester"): 
    Who/What is it?:
        Web browsers (Chrome, Firefox), IoT devices, Mobile apps (Instagram, WhatsApp), Desktop Software 
    
    Main Responsibilities:
        Display the user interface (UI), Collect input from the user (clicks, typing, etc.), Send HTTP requests to the server, Show the results to the user (e.g., render HTML, update app screens)

    Technologies Used:
        HTML/CSS/JavaScript (web), Swift/Kotlin (mobile), React/Vue/Flutter (for dynamic UI), Axios, Fetch API, Retrofit, etc. for HTTP requests
    
    From SERVER-Side("The Responder/Processor"):
    Who/What is it?:
        Web servers (Apache, Nginx), Databases (MySQL, MongoDB, PostgreSQL), Application servers (Node.js, Django, Flask, Spring Boot, etc.)

    Main Responsibilities: 
        Receive HTTP requests, Process logic (check a database, apply rules, do computations), Generate a response (HTML, JSON, file, etc.), Send the response back to the client  

    Technologies Used:
        It searches its database for images related to related stuffs, Packages the result (in HTML or JSON), Sends it back to the browser


    📦 Common HTTP Methods:
    {GET}: Retrieve data from the server.(like a web page)
    {POST}: Send data to the server (like a form)
    {PUT}: Update existing data
    {DELETE}: Delete data

    🧭 Visual Flow Example:

        User clicks "Search" in browser
            ↓
        CLIENT → Sends HTTP GET request → SERVER
            ↓                                 ↓
               ← Server fetches data ← Database
            ↓
        SERVER → Sends HTTP response (HTML/JSON) → CLIENT
            ↓
        Browser displays search results to the user

    ✏️HTTP-JSON Example 
        ✅ GET – Fetch Favorites:
            Client Request:
             GET /favorites
            
            Server Response:
             ["Istanbul", "Ankara", "London"]

        ✅  POST – Add a New Favorite City:
             Client Request:
              POST /favorites
              Content-Type: application/json

             Server Request:
              {
               "city": "Izmir"
              }
        
        ✅  PUT – Update a Favorite City:
             Use case: User wants to update "Izmir" to "Bursa":

             Client Request:
              PUT /favorites
              Content-Type: application/json

              {
                "oldCity": "Izmir",
                "newCity": "Bursa"
              }
             
             Server Response:
              {
                "message": "Favorite updated"
              }   
            
        ✅  DELETE – Remove a City from Favorites:
             Client Request:
               DELETE /favorites
               Content-Type: application/json

              {
                "city": "Ankara"
              }

             Server Response:
              {
                "message": "City deleted from favorites"
              }

    One-Time vs Continuous Communication
    HTTP is stateless: each request is independent.
    But technologies like WebSockets allow continuous, two-way communication, like in real-time chat apps.


    Response Status Codes:
    1XX: Informational Response – the request was received, continuing process,
    2XX: Successful – the request was successfully received, understood, and accepted,
    3XX: Redirection – further action needs to be taken in order to complete the request,
    4XX: Client Error – the request contains bad syntax or cannot be fulfilled,
    5XX: Server Error – the server failed to fulfil an apparently valid request.
    '''