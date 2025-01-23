import skia

# Example text with emojis
text = "We are happy today 😀 !"
font_size = 18
canvas_width, canvas_height = 500, 200


# Create a Skia surface and canvas
surface = skia.Surface(canvas_width, canvas_height)
canvas = surface.getCanvas()

# Set background color
canvas.clear(skia.ColorWHITE)
    
# Define font and paint
paint = skia.Paint(AntiAlias=True, Color=skia.ColorBLACK)

# Draw text using Arial
canvas.drawTextBlob(skia.TextBlob(text, skia.Font(skia.Typeface( "Arial" , skia.FontStyle.Bold()))), 20, 50, paint)


# Save output to PNG

img = skia.Image.fromarray(canvas.toarray(colorType=skia.ColorType.kRGBA_8888_ColorType), colorType=skia.ColorType.kRGBA_8888_ColorType)
img.save("img.png")