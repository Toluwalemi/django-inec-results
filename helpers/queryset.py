from bincom.models import States, Lga, Ward, PollingUnit


def get_state_data(state_id: int) -> dict:
    """
    Function to get all details relating to States model
    i.e LGA, Wards, and Polling units
    @param state_id:
    @return: returns a dictionary of the details
    """
    state = States.objects.filter(state_id=state_id)
    error_msg = {
        'status': 'fail',
        'message': 'Invalid ID'
    }
    if not state:
        return error_msg
    if state.exists():
        lga = Lga.objects.filter(state_id=state[0].state_id)  # assumes just one state in table- Delta
        ward = Ward.objects.filter(lga_id__in=lga.values('lga_id'))
        pollings = PollingUnit.objects.filter(ward_id__in=ward.values('ward_id'))
        response_object = {'state': state, 'lga': lga,
                           'ward': ward, 'pollings': pollings}

        return response_object
