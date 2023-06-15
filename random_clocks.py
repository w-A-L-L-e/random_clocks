import random
import math
from reportlab.pdfgen import canvas

# Function to draw an analogue clock with given time
def draw_analogue_clock(c, x, y, hour, minute):

    c.setLineWidth(1) 
    # Draw clock face
    c.circle(x, y, 50)

    c.setFont("Helvetica", 10)
    # Draw hour lines
    for i in range(12):
        angle = 2 * math.pi * (i / 12.0)
        c.line(x + 45 * math.sin(angle), y + 45 * math.cos(angle),
               x + 40 * math.sin(angle), y + 40 * math.cos(angle))

        disp_hour = i
        if disp_hour == 0:
            disp_hour = 12
        c.drawCentredString(x + 35 * math.sin(angle), (y-4) + 35 * math.cos(angle), f"{disp_hour}")

    # Draw minute lines
    for i in range(60):
        angle = 2 * math.pi * (i / 60.0)
        c.line(x + 48 * math.sin(angle), y + 48 * math.cos(angle),
               x + 46 * math.sin(angle), y + 46 * math.cos(angle))

    # Draw hour hand
    hour = float(hour % 12)
    hour_angle = 2 * math.pi * ((hour / 12.0) + (minute / 60.0 / 12.0))

    c.setLineWidth(1) 
    c.line(x, y, x + 25 * math.sin(hour_angle), y + 25 * math.cos(hour_angle))
    c.setLineWidth(2) 
    c.line(x, y, x + 25 * math.sin(hour_angle), y + 25 * math.cos(hour_angle))

    # Draw minute hand
    minute_angle = 2 * math.pi * (minute / 60.0)
    c.setLineWidth(1) 
    c.line(x, y, x + 40 * math.sin(minute_angle), y + 40 * math.cos(minute_angle))
    c.setLineWidth(2) 
    c.line(x, y, x + 40 * math.sin(minute_angle), y + 40 * math.cos(minute_angle))

# Create a new PDF document
c = canvas.Canvas("analogue_clocks.pdf")

# Generate 16 random times and draw the clocks with digital time
c.setFont("Helvetica", 10)
hours = []
minutes = []
for i in range(16):
    # Generate random hour (0-23)
    hour = random.randint(0, 23)
    hours.append(hour)

    # Generate random minute (round to the nearest multiple of 5)
    minute = random.randint(0, 11) * 5
    minutes.append(minute)

    # Calculate the position for the clock on the page
    x = 80 + (i % 4) * 150
    y = 700 - (i // 4) * 180

    # Draw the analogue clock
    draw_analogue_clock(c, x, y, hour, minute)

    # Draw the time label
    time_label = "{:02d}:{:02d}".format(hour, minute)
    c.drawCentredString(x, y - 70, time_label)

# Create a new page for clocks without digital time
c.showPage()

# Generate 16 random times and draw the clocks without digital time
for i in range(16):
    # Generate random hour (0-23)
    #hour = random.randint(0, 23)
    hour = hours[i]

    # Generate random minute (round to the nearest multiple of 5)
    #minute = random.randint(0, 11) * 5
    minute = minutes[i]

    # Calculate the position for the clock on the page
    x = 80 + (i % 4) * 150
    y = 700 - (i // 4) * 180

    # Draw the analogue clock
    draw_analogue_clock(c, x, y, hour, minute)

    c.drawCentredString(x, y - 70, "_____________")

# Save the PDF document
c.save()
