from pptx import Presentation
from pptx.util import Inches
import os

# Function to save content to a PowerPoint file
def save_content_to_ppt(content, chart_path, filename="result/Profiler_Report.pptx"):
    # Ensure the result directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    # Create a PowerPoint presentation
    prs = Presentation()
    
    for title, text in content.items():
        # Add a slide for each section
        slide = prs.slides.add_slide(prs.slide_layouts[1])
        title_placeholder = slide.shapes.title
        content_placeholder = slide.placeholders[1]

        # Set the title and content
        title_placeholder.text = title
        content_placeholder.text = text

        # Add the chart to the Financials slide
        if title == "Financials" and os.path.exists(chart_path):
            slide.shapes.add_picture(chart_path, Inches(1), Inches(2), width=Inches(4))

    # Save the presentation
    prs.save(filename)
