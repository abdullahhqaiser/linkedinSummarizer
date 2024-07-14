def clean_response(res):
    keys_to_remove = [
        "urn",
        "profilePicture",
        "backgroundImage",
        "languages",
        "fullPositions",
        "givenRecommendation",
        "givenRecommendationCount",
        "receivedRecommendation",
        "receivedRecommendationCount",
        "volunteering",
        "supportedLocales",
        "multiLocaleFirstName",
        "multiLocaleLastName",
        "multiLocaleHeadline",
        "projects",
        "honors",
    ]
    education_keys = ["start", "end", "fieldOfStudy", "degree", "schoolName"]
    position_keys = [
        "companyName",
        "title",
        "description",
        "employmentType",
        "start",
        "end",
    ]
    certifications_keys = ["name", "start", "end"]

    updated_dict = {
        key: value for key, value in res.items() if key not in keys_to_remove
    }
    updated_dict["educations"] = [
        {key: value for key, value in d.items() if key in education_keys}
        for d in updated_dict["educations"]
    ]
    updated_dict["position"] = [
        {key: val for key, val in d.items() if key in position_keys}
        for d in updated_dict["position"]
    ]
    updated_dict["certifications"] = [
        {key: value for key, value in d.items() if key in certifications_keys}
        for d in updated_dict["certifications"]
    ]
    updated_dict = {
        key: value
        for key, value in updated_dict.items()
        if value not in [None, "", 0, [], {}, False]
    }
    return updated_dict
