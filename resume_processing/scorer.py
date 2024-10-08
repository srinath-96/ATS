def score_resume(parsed_info):
    # Implement scoring logic based on parsed information
    # This is a placeholder implementation
    score = 0
    if parsed_info.get('education'): score += 20
    if parsed_info.get('work_experience'): score += 30
    if parsed_info.get('skills'): score += 20
    # Add more scoring criteria as needed
    return min(score, 100)  # Ensure score doesn't exceed 100