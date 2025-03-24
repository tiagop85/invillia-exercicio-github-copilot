# ...existing code...

@app.post("/signup_for_activity")
def signup_for_activity(activity_id: int, email: str):
    # ...existing code...
    
    # Validate if the student is already signed up
    if email in activity["participants"]:
        raise HTTPException(status_code=400, detail="Student is already signed up for this activity")
    
    # Add student
    activity["participants"].append(email)
    # ...existing code...
