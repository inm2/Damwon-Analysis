# Damwon-Analysis
Analysis of League of Legends LCK team, DAMWON Gaming, for Spring and Summer 2020 

## Introduction
League of Legends (LoL) is a 5v5 multiplayer online battle arena (MOBA) developed and published by Riot in 2009. On the game's esports side, 2020 marks the [10th Anniversary](https://www.espn.com/esports/story/_/id/29954672/ten-years-worlds-league-legends-world-championship-oral-history) of LoL World Championships.

As someone who wants to use data science and machine learning towards esports, I enjoy the way the game can be broken down statistically. This project is my introductory attempt to learn more about how in-game data can be formed and be used to make inferrences about a team or player. 

This year (2020), DAMWON Gaming, the number 1 team from LoL Champions Korea (LCK) won the League of Legends World Championship. I wanted to use the data from their matches to be able to snapshot the year they had and to try to take an analytical dive into some of their successes.   

DISCLAIMER: I try to keep up with League of Legends as much as I can on the competitive scene, but my in-game knowledge is pretty low. This project will serve two purposes: 1. To make myself more informed about the game on at least a statistical level, and 2. to show some competency with coding in SQL and Python. 

ACKNOWLEDGEMENT: I'd like to thank my friend Quinn for helping me figure out what type of data would be valuable to visualize. 

## Resources Used 
- [DAMWON statistics by player](https://lol.gamepedia.com/DAMWON_Gaming/Statistics/2020)    
- [Kamal Chouhbi - Inspiration for doing this project](https://towardsdatascience.com/what-is-like-to-be-a-data-scientist-with-a-passion-for-gaming-43c067ad6415)  
- [Oracle's Elixr - Includes all of the data I used for the project](https://oracleselixir.com/tools/downloads)  
- SQL  
- Python 3.7 (Spyder IDE)  

## Links to Projects
1. [Damwon's Spring and Summer Seasons At a Glance](https://github.com/inm2/Damwon-Analysis/blob/main/1%20-%20Damwon%20Season%20At%20A%20Glance.ipynb)  
2. [Factors of Dominance - Gold Difference](https://github.com/inm2/Damwon-Analysis/blob/main/2%20-%20Factors%20of%20Dominance.ipynb)  

## League of Legends Overview
League of Legends is a 5v5 multiplayer game. The objective of the game's flagship mode, Summoner's Rift, is to destroy an enemy's base or Nexus. To do so, players on each team start on one side and must traverse and destroy any obstacles, in the form of enemies, turrets, and inhibitors, to reach an opponent's Nexus. 

[Map Overview](https://www.google.com/search?q=league+of+legends+map+overview+top+bottom+middle&tbm=isch&ved=2ahUKEwiKu8KS6abtAhXUEFMKHYFHCPgQ2-cCegQIABAA&oq=league+of+legends+map+overview+top+bottom+middle&gs_lcp=CgNpbWcQAzoECAAQHlCQSlixaWCQamgAcAB4AIABbIgB-AuSAQQxNi4ymAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=xxbDX8q7CtShzAKBj6HADw&bih=692&biw=1376&client=firefox-b-1-d#imgrc=GaycUvqvzNGygM)

The five roles that compose each team are: Top, Mid, Jungle, Attack Damage Carry (ADC), and Support. 

## Where to go from here?
In the future, I want to create my own linear/logitistic regression model(s) to see if the prediction of outcomes on a game-by-game basis for Damwon can be accurately modeled. This model will require future studying of League's mechanics. I wanted to include it for this version of text, but MySQL somehow deleted during import the Drake and Baron data, as well as any tower destruction data. If I can't figure out why the import is messing up these values, I will have to create a dataframe in Python and do my parameterization and filtering through Pandas. This page will be updated with any future info.  
