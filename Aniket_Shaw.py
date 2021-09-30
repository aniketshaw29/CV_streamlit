#code pkg
import streamlit as st
from PIL import Image



col1, col2 = st.columns(2)
img=Image.open('images/aniket.jpg')
col1.image(img,width=300)
col2.title("Aniket Shaw")
col2.markdown("Hi, I am a Computer Science student with a Commerce background, currently pursuing BCA from [Institute of Engineering and Management (IEM)](https://iem.edu.in/). I aspire to become a Software developer. I have completed my primary and secondary education from [Douglas Memorial Higher Secondary School (DMHSS)](https://www.dmhss.org/) which is affilated to [Council for Indian School Certificate (CISE)](https://www.cisce.org/).")
st.markdown("-----")


st.write('Hey there! This is Aniket. I am in the sophomore year of my college majoring in Computer Science. Life has thoroughly taught me, again and again, to be opportunistic, and I believe I have picked it up quite well. Working smart is my second nature, for instance how efficiently the task is done is more important to me than just getting the task done. Majoring in Computer Science, I am an enthusiast for the cutting-edge inventions and innovations in this respective field and look forward to having my hands on them someday. Being from a commerce background in high school is indeed a great advantage because I started programming while I was in junior high so when I was introduced how businesses operates, I could clearly bridge the gap between IT and Business.')
st.write('One thing that coding has taught me is that there are numerous ways of circumventing a problem and debugging it, this eventually broadened my perspective and helped me carve out that open-mindedness. Not only does that help me encompass the dynamic approach of coding but also opens up a lot of creative faucets in my life. Although I am a team player, my learning curve is different from others as I first prefer self-study and then I opt for group discussion. Somewhere I believe that it’s never too late to venture out for something. We can become whoever we want to, the only thing that is required is COURAGE. There’s no ending to life’s learning and you never know who might end up giving you a life-changing advice, hence, I respect the opinion of everyone irrespective of their age or their designation. This makes me need an extra pair of eyes at times, which turns out to be the most important reality check to me. It helps me get rid of my biases and prejudices.')
st.write('One of the major takeaways that coding has taught me is that I cannot make all the mistakes myself and go through the process of hit and trial with everything, which means, not only I get to learning from my own mistakes but also, I get to learn from other’s mistakes. Now that is not only a valuable lesson in coding but in life as well, Chanakya was right! So far into life, I cannot emphasize more, the importance of good time management. This makes me the person who cuts to the chase and likes being straightforward with my approach.')
st.write('My ending note would be: Discipline, Dedication, Perseverance and a little bit of Faith can move the biggest mountains in life, we only need to have the courage to set forth for the venture we are sceptical about. If you’ve read so far, know that we have already met.')
st.markdown("-----")


st.sidebar.markdown("## Side Panel" )
st.sidebar.markdown("This is my portfoli which is made using the framework streamlit. You can browse around using this panel to explore more about me.")
st.sidebar.subheader(' Quick  Explore')
if st.sidebar.checkbox('Basic info'):
    st.title('About me:')
    st.write('Name - Aniket Shaw')
    st.write('Age - 19')
    st.write('Gender - Male')
    st.write('Education - Undergraduate')
    st.write('Location - Barrackpore, Kolkata, West Bengal, India')
    st.write('Languages - English, Hindi, Bengali')
    st.markdown("-----")

if st.sidebar.checkbox('Interest & hobbies'):
    st.title('Interest in:')
    st.write('Software development')
    st.write('Machine Learning')
    st.write('Android Development')

    st.write('Education - Undergraduate')
    st.title('Hobbies:')
    st.write('Swimming')
    st.write('Travelling')
    st.write('Gyming')
    st.write('Cooking')
    st.write('Gaming')
    st.markdown("-----")

if st.sidebar.checkbox('Strength & Weakness'):
    st.title('Strength:')
    st.write('Problem Solving')
    st.write('Public Speaking')
    st.write('Time Management')
    st.write('Presentation')
    st.write('Communication')
    st.write('Team Player')
    st.write('Good listener')

    st.title('Weakness:')
    st.write('Overthinking Problem')
    st.write('Trust Issues')
    st.write('Old School')
    st.markdown("-----")

if st.sidebar.checkbox('My Education Qualification'):
    st.title('ICSE [Class X]')
    st.write('Passing year - 2018')
    st.write('Percentage - 75%')
    st.write('School - Douglas Memorial Higher Secondary School')

    st.title('ISC [Class XII]')
    st.write('Passing year - 2020(by 12th march)')
    st.write('Percentage - 80%')
    st.write('School - Douglas Memorial Higher Secondary School')

    
    st.title('Undergraduation [1st Year] ')
    st.write('Passing year - 2021')
    st.write('SGPA - 9.6')
    st.write('College - Institute of Engineering and Management')
    st.markdown("-----")
    
if st.sidebar.checkbox('Coding Skills'):
    st.title('Programming languages:')
    st.write('Java')
    st.write('Python')
    st.write('SQL')
    st.write('C++')

    st.title("Other Domains:")
    st.write('Database(RDBMS) - Oracle SQL, Mysql')
    st.write('Web Development - HTML,CSS,PHP,JS,Jquery')
    st.write('Frameworks - Bootstrap, Streamlit')
    st.write('Unix Shell scripting')
    st.write('Xilinx ISE')
    st.write('MS Office')
    st.markdown("-----")

if st.sidebar.checkbox('Work ex'):
    st.title("Work experience:")
    st.write('Web Developer at CrudeBits  -  3months(2021)')
    st.markdown("-----")


if st.sidebar.checkbox('Contact me'):
    st.title("Professional:")
    st.write('Email - aniketshawwork@gmail.com')
    st.write('Mobile - 6290361967')
    st.write('[Linkedin](https://www.linkedin.com/in/aniketshaw/)')
    st.write('[Github](https://github.com/aniketshaw29)')
    st.write('[Personal Site](https://aniketshaw29.github.io/AniketShawResume/)')

    st.title("Social:")
    st.write('[Instagram](https://www.instagram.com/aniiiii_29/)')
    st.write('[Facebook](https://www.facebook.com/aniket.shaw.71404/)')
    st.write('[Twitter](https://twitter.com/Aniket_Shaw_)')

    st.markdown("-----")

