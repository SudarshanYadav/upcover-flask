import datetime 

def pre_proc(suburb,number_of_claims_made,birth_year,age_at_licence):
	new_dict = {}
    current_year = datetime.datetime.now().year
    current_age = current_year - birth_year
    license_age = current_age - age_at_licence
    number_of_calims_made = number_of_claims_made
    suburb_dict = {
        'Marrickville'		: 1,
        'North Manly'		: 2,
        'Pymble'			: 3,
        'South Granville'	: 4,
        'Willoughby'		: 5
    }
    suburb = suburb_dict[suburb]
    return [suburb,number_of_calims_made,current_age,license_age] 
