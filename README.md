This is version 2 of the Ludo App. Version 1 can be read [here](https://github.com/fidanazhan/django-ludo-1ver).

# LUDO - V2
Sport App where users can host or participate for sport games in their local area. The second version of the app is created using Django and Django Rest Framework for the backend while use Vue.js for the frontend. 

## TABLE OF CONTENTS
  
  -  [Overview](#overview)
  -  [Technology](#technology)
  -  [Requirement](#requirement)
  -  [Screenshot](#screenshot)
  -  [Status](#status)
  -  [Contact](#contact)

## **OVERVIEW**

Ludo is a sport app where users can host and participate in a sport game in their local area. This simple app was created because there was a difficulty in gathering people to play certain sports. A host (people who host a game) can create a game, set venue and date before accepting any join request from other users. Participants (users who want to join) can see the sport type, venue, location, date and price to join before they send a join request to the host. With this app, users can play their favorite sport with strangers and can make new friends.

## **TECHNOLOGY** 

- Framework/Stack : Django, Django Rest Framework, Vue.js, HTML, CSS, Tailwind CSS, Javascript, ORM, Faker 
- Database : PostgreSQL
- System Architecture : Monolithic (with REST API)
- Software Architecture : MVT

## **REQUIREMENT**

- User can see list of games
- (Host) User can create new game
- (Participant) Users can send requests to join the game.
- (Host) Users can approve or decline the join request.
- (Participant) User can unsent the join request.
- (Host) Users can remove the player from the game.
- (Participant) Users can unjoin the game.
- Users can see the list of games that they have joined or games that they will play soon.
- Send notifications to the user.
- Users can see a list of received notifications.

## SCREENSHOT

#### 1- Dashboard View 
Place where users can see their games played, number of games created and number of join requests sent. The two boxes in the center will be graphs that show analytics for the games played by the user (not completed yet). The table below the graphs is the data of incoming games that the user will play. 
The red box and blue box will be graphs that show statistics for each user (still under development).

![Dashboard View](https://user-images.githubusercontent.com/108860416/191573837-0d73d3c7-c63c-4afd-a6db-816d1fa0d709.PNG)
&nbsp;

#### 2 - Host - Game List View
Page where the users can see the list of games they created. When they click to the yellow button, they will 
be redirected to Host - Game Detail View. The ‘Edit’ button will display the Edit Game Modal and ‘Delete’ button will show the Delete Game Modal.

![Host - Game List View](https://user-images.githubusercontent.com/108860416/191573878-4f8938e5-3959-4959-a341-4438103882bd.PNG)
&nbsp;

#### 3 - Host - Game Detail View
The details of the game are displayed on this page. On this page, there are also ‘Edit’ and ‘Delete' buttons. There is also a list 
of approved players by the host at ‘Player Joined’ line. The host can remove the player by clicking the ‘Remove Player’ button. At the ‘Join Request’ line, 
the list of requested users for this game are shown here. The host can approve or decline the join request by clicking the ‘Accept’ and ‘Reject’ buttons.

![Host - Game Detail View](https://user-images.githubusercontent.com/108860416/191573898-55f40eea-c3cb-4275-9bc1-efea5b446849.PNG)
&nbsp;

#### 4 - Host - Game Edit Modal
![Host - Edit Game Modal](https://user-images.githubusercontent.com/108860416/191573908-8b9b2f32-fdee-4bd1-9255-df6e7ee4481f.PNG)
&nbsp;

#### 5 - Host - Game Delete Modal
![Host - Delete Game Modal](https://user-images.githubusercontent.com/108860416/191573914-b316502d-95f7-4826-aad1-b822253c6f3d.PNG)
&nbsp;

#### 6 - Participant - Join Request View
Page that shows a list of requests sent by the user to join games. Users can cancel the request by clicking the 'Cancel Request' button. 

![Participant - Join Request List](https://user-images.githubusercontent.com/108860416/191574048-a9d69ad5-ba5b-499a-990d-130d68a653a2.PNG)
&nbsp;

#### 7 - Game List View 
Page where users can see available games for them to join. They can also create a new game by clicking the ‘Create Game’ button on the top left corner of the 
table. The Create Game Modal will be displayed. Users can click the ‘More Detail’ button to know more about the game and send join request (Game Detail Modal will
be displayed with 'Join' button).

![Game List View](https://user-images.githubusercontent.com/108860416/191573966-1b063bb5-1726-41b7-9bfe-13627509a994.PNG)
&nbsp;

#### 8 - Create Game Modal
![Create Game Modal](https://user-images.githubusercontent.com/108860416/191574125-af746ecb-bc45-4ca9-9068-2962c6312edf.PNG)
&nbsp;

#### 9 - Game Detail and Join Request Modal
![Game Detail And Join Request Modal](https://user-images.githubusercontent.com/108860416/191574110-46cd8bed-9021-49f1-88b8-8e57087a613f.PNG)
&nbsp;

**The Notification page**, **Competition page** and **Settings page* is still in development.

## STATUS

Not Completed. Ongoing development.

## CONTACT 

Created by [Fidan Azhan](https://github.com/fidanazhan) - feel free to contact me!


