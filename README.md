# weather-analysis
This project is only for demo purpose for the hiring process by TransOrg.
<p>
Basic Requirements to run the app
<li>Django </li>
<li>Python3 </li>
</p>
<p>
Install Virtual Environment before setting up the project, then follow the following steps
<ol> pip install -r requirements.txt </ol>
<ol> python manage.py makemigrations </ol>
<ol>python manage.py migrate </ol>
<ol> python manage.py createsuperuser </ol>
</p>
<p>
Regarding the task1, the requirement is that on the basis of time range we have to either plot the temperature or the humidity, the API that I am using doesn't provide humidity data(limitation) so the graph the plotted always for temperature, also the task mentioned that make a dropdown, for that I think that making an autocomplete will be good idea.
</p>
<p>
I have used by default 4 cities namely: Delhi, Bengaluru, Pune, Gurgaon to get the data.
</p>
<p>
Regarding the task2, the requirement states that the stations that has been added can be choosen from the dropdown, i think that it will not be a good idea to mix cities along with weather stations added, which can further lead to confusion. So  for the task2, i have just saved the weather stations that the user will chose after selecting the city. The graph can also be plotted for the same.
</p>
<p>
If you have any problem, regarding running the app, kindly drop a mail at pranavpuri.p@hotmail.com
</p>
