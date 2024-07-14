import random
import random
import tkinter as tk

# List of notes

notes = [
    "The object isn’t to make art, it’s to be in that wonderful state which makes art inevitable. Robert Henri",
    "Creativity doesn’t exclusively relate to making art. We all engage in this act on a daily basis. To create is to bring something into existence that wasn’t there before.",
    "Artists who are able to continually create great works throughout their lives often manage to preserve childlike qualities. Practicing a way of being that allows you to see the world through uncorrupted, innocent eyes can free you to act in concert with the universe’s timetable.",
    "If something strikes me as interesting or beautiful, first I live that experience. Only afterward I might attempt to understand it.",
    "The ability to look deeply is the root of creativity. To see past the ordinary and mundane and get to what might otherwise be invisible.",
    "Each of us has a container within. It is constantly being filled with data. It holds the sum total of our thoughts, feelings, dreams, and experiences in the world. Let’s call this the vessel. Information does not enter the vessel directly like rain filling into a barrel.",
    "To navigate our way through this immense world of data, we learn early in life to focus on information that appears essential or of particular interest and to tune out the rest.",
    "As artists, we seek to restore our childlike perception: a more innocent state of wonder and appreciation not tethered to utility or survival.",
    "We aren’t creating to produce or sell material products. The act of creation is an attempt to enter a mysterious realm. A longing to transcend. What we create allows us to share glimpses of an inner landscape, one that is beyond our understanding. Art is our portal to the unseen world.",
    "The spiritual world provides a sense of wonder and a degree of open-mindedness not always found within the confines of science",
    "Notice connections and consider where they lead",
    "Look for what you notice, but no one else sees.",
    "Widening one’s scope allows for more moments of interest to be noticed and collected, building a treasury of material to draw from later.",
    "Awareness needs constant refreshing. If it becomes a habit, even a good habit, it will need to be reinvented again and again. Until one day, you notice that you are always in the practice of awareness, at all times, in all places, living your life in a state of constant openness to receiving.",
    "Consider submerging yourself in the canon of great works. Read the finest literature, watch the masterpieces of cinema, get up close to the most influential paintings, and visit architectural landmarks.",
    "Of all the great works that we can experience, nature is the most absolute and enduring. We can witness it change through the seasons. We can see it in the mountains, the oceans, the deserts, and the forest. We can watch the changes of the moon each night and the relationship between the moon and the stars.",
    "There is never a shortage of awe and inspiration to be found outdoors",
    "Nature transcends our tendencies to label and classify, to reduce and limit. The natural world is unfathomably more rich, interwoven, and complicated than we are taught, and so much more mysterious and beautiful.",
    "The person who makes something today isn’t the same person who returns to the work tomorrow.",
    "Our inner world is every bit as interesting, beautiful, and surprising as nature itself. It is, after all, born of nature. When we go inside, we are processing what’s going on outside. We’re no longer separate. We’re connected. We are one",
    "Keeping a dream journal might be of use. Place a pen and paper next to the bed, and as soon as you wake up, begin writing immediately with as much detail as possible before doing anything else. Try to limit any unnecessary movement.",
    "I’m strongly affected by the sun. When it’s a bright day, I feel energized. When it’s gloomy, I’m gloomy. On those overcast days, it helps to tune in to the fact that the sun is still there. It’s just hidden behind a thicker layer of clouds. At noon, the sun is high in the sky, regardless of how light or dark it is outside.",
    "In the same way, regardless of how much we’re paying attention, the information we seek is out there. If we’re aware, we get to tune in to more of it. If we’re less aware, we miss it. When we miss it, it really does pass us by.",
    "Tomorrow presents another opportunity for awareness, but it’s never an opportunity for the same awareness.",
    "Oceans are fine locations to receive direct transmissions from the universe. If instead, you want to tune in to the collective consciousness, you might sit in a busy spot with people coming and going and experience Source as filtered through humanity. This secondhand approach is no less valid.",
    "It’s better to follow the universe than those around you.",
    "Flaws are human, and the attraction of art is the humanity held in it. If we were machinelike, the art wouldn’t resonate. It would be soulless. With life comes pain, insecurity, and fear",
    "If a creator is so afraid of judgment that they’re unable to move forward, it might be that the desire to share the work isn’t as strong as the desire to protect themselves. Perhaps art isn’t their role. Their temperament might serve a different pursuit. This path is not for everyone. Adversity is part of the process.",
    "If you see tremendous beauty or tremendous pain where other people see little or nothing at all, you’re confronted with big feelings all the time. These emotions can be confusing and overwhelming. When those around you don’t see what you see and feel what you feel, this can lead to a sense of isolation and a general feeling of not belonging, of otherness.",
    "How do we move forward, considering the stories we tell ourselves? One of the best strategies is to lower the stakes. We tend to think that what we’re making is the most important thing in our lives and that it’s going to define us for all eternity. Consider moving forward with the more accurate point of view that it’s a small work, a beginning. The mission is to complete the project so you can move on to the next. That next one is a stepping-stone to the following work. And so it continues in a productive rhythm for the entirety of your creative life.",
    "Realizing you are fortunate to be in a position that allows you to create and in some cases, get paid to do what you love might tip the balance in favor of the work.",
    "Doubting yourself can lead to a sense of hopelessness, of not being inherently fit to take on the task at hand. All-or-nothing thinking is a non-starter."
]

# Function to select a random note
def get_random_note():
    return random.choice(notes)

# Function to generate a random quote and display it
def generate_quote():
    quote = get_random_note()
    quote_label.config(text=quote)

# Create the main window
window = tk.Tk()
window.title("Random Quote Generator")

# Create a label to display the quote
quote_label = tk.Label(window, wraplength=400, font=("Arial", 12))
quote_label.pack(pady=20)

# Create a button to generate a random quote
generate_button = tk.Button(window, text="Generate Quote", command=generate_quote)
generate_button.pack(pady=10)

# Start the main event loop
window.mainloop()
# List of notes
