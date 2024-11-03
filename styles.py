small_button_css = """
<style>
/* Style for a small Streamlit button */
.stButton > button {
    width:100%;
    border-radius: 4px; /* Border radius for button */
    font-size: 0.8rem; /* Set a smaller font size */
    padding:0; /* Adjust padding for a smaller button */
    background-color: transparent; /* Transparent background */
    color: white; /* Text color */
    border: none; /* Remove border */
    cursor: pointer; /* Pointer cursor on hover */
    transition: background-color 0.3s ease, color 0.3s ease; /* Transition for hover effect */
    text-align: left; /* Align text to the left */
    position: relative; /* Positioning for hover effect */
}

/* Hover effect */
.stButton > button:hover {
    background-color: rgba(255, 255, 255, 0.1); /* Slight white background on hover */
    color: #fff; /* Maintain text color */
}

/* Style for the delete button */
.delete-button {
    display: none; /* Hide delete button by default */
    position: absolute; /* Position delete button */
    right: 0; /* Align to the right */
    background-color: red; /* Background color for delete button */
    color: white; /* Text color */
    border: none; /* Remove border */
    padding: 0.2rem 0.5rem; /* Padding for delete button */
    font-size: 0.7rem; /* Smaller font size */
    border-radius: 4px; /* Border radius */
}

/* Show delete button on hover */
.stButton:hover .delete-button {
    display: inline-block; /* Show delete button on hover */
}
</style>
"""


