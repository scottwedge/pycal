import datetime
import json

import event


def display(start_date: list = None, end_date: list = None,
            long: bool = False) -> dict:
    '''Display events for specified date(s).'''
    if start_date == None:
        display_start_date = datetime.date.today()
    elif start_date != None:
        display_start_date = datetime.date(start_date[0], start_date[1], start_date[2])
    display_start_date = display_start_date.isoformat()
    if end_date:
        display_end_date = datetime.date(end_date[0], end_date[1], end_date[2])
        display_end_date = display_end_date.isoformat()

    filename = '/Users/arek/.termical/termical_data.json'
    with open(filename) as f:
        import_dates = json.load(f)

    import_dates_list = []
    for date in import_dates:
        import_dates_list.append(date)

    display_start = import_dates_list.index(display_start_date)
    if end_date:
        display_end = import_dates_list.index(display_end_date) + 1
        display_dates = import_dates_list[display_start:display_end]
    elif not end_date:
        display_dates = import_dates_list[display_start]

    
    display_dict = {}
    if type(display_dates) == str:
        display_dict[display_dates] = import_dates[display_dates]
    else:
        for date in display_dates:
            display_date_schedule = import_dates[date]
            display_dict[date] = display_date_schedule
    return display_dict

def schedule(title: str, start_date: list, end_date: list = None, location: list
             = '', note: list = '') -> str:
    '''Schedule an event.'''

    # Convert dates from function call into date objects and iso strings
    # eventually.
    if start_date:
        schedule_date = datetime.datetime(*start_date)
    elif not start_date:
        schedule_date = datetime.date.today()
    schedule_date = schedule_date.isoformat()
    if end_date:
        schedule_end_date = datetime.datetime(*end_date)
    elif not end_date:
        schedule_end_date = schedule_date

    filename = '/Users/arek/.termical/termical_data.json'
    with open(filename) as f:
        import_dates = json.load(f)

    # Convert list arguments into strings.
    if type(title) == list:
        separator = ' '
        title = separator.join(title)
    if type(note) == list:
        separator = ' '
        note = separator.join(note)

    event = termical_event.Event(title=title, start_date=schedule_date,
                                 end_date=schedule_end_date,
                                 location=location, note=note)
    import_dates_list = []
    for date in import_dates:
        import_dates_list.append(date)

    iter_start = schedule_date.split('T')
    iter_start = iter_start[0]
    iter_end = schedule_end_date.split('T')
    iter_end = iter_end[0]
    schedule_start = import_dates_list.index(iter_start)
    schedule_end = import_dates_list.index(iter_end) + 1
    schedule_dates = import_dates_list[schedule_start:schedule_end]
    
    # Schedule event.
    for date in schedule_dates:
        import_dates[date][event.title] = {}
        for attribute in event:
            import_dates[date][event.title][attribute[0]] = attribute[1]

    with open(filename, 'w') as f:
        json.dump(import_dates, f, indent=4)

    message = f"{event.title} has been scheduled to {event.start_date} -"
    message += f" {event.end_date}."
    return message

def remove(title: str, date: list, end_date: list = None) -> list:
    '''Remove an event.'''
    remove_date = datetime.date(date[0], date[1], date[2])
    remove_end_date = datetime.date(end_date[0], end_date[1], end_date[2])
    remove_date = remove_date.isoformat()
    remove_end_date = remove_end_date.isoformat()
    filename = '/Users/arek/.termical/termical_data.json'
    with open(filename) as f:
        import_dates = json.load(f)
    import_dates_list = []
    for date in import_dates:
        import_dates_list.append(date)

    shortcut_start = import_dates_list.index(remove_date)
    shortcut_end = import_dates_list.index(remove_end_date) + 1
    shortcut = import_dates_list[shortcut_start:shortcut_end]

    if type(title) == str:
        pass
    elif type(title) == list:
        separator = ' '
        title = separator.join(title)

    return_messages = []
    for date in shortcut:
        try:
            del import_dates[date][title]
        except KeyError:
            error_message = f"Error, there is no such event '{title}' on {date}"
            return_messages.append(error_message)
        else:
            with open(filename, 'w') as f:
                json.dump(import_dates, f, indent=4)
            message = f"{title} on {date} has been removed."
            return_messages.append(message)
    return return_messages

def move(event: str, source_start_date: list = None, source_end_date: list = None,
         target_start_date: list = None, target_end_date: list = None, location:
         list = None, note: list = None) -> list:
    '''Move - reschedule an event.'''
    move_source_start_date = datetime.date(source_start_date[0],
                                           source_start_date[1],
                                     source_start_date[2])
    move_source_start_date = move_source_start_date.isoformat()
    move_source_end_date = datetime.date(source_end_date[0], source_end_date[1],
                                         source_end_date[2])
    move_source_end_date = move_source_end_date.isoformat()

    if target_start_date and target_end_date:
        move_target_start_date = datetime.date(target_start_date[0],
                                               target_start_date[1],
                                               target_start_date[2])
        move_target_start_date = move_target_start_date.isoformat()
        move_target_end_date = datetime.date(target_end_date[0],
                                             target_end_date[1],
                                             target_end_date[2])
        move_target_end_date = move_target_end_date.isoformat()
    filename = '/Users/arek/.termical/termical_data.json'
    with open(filename) as f:
        import_dates = json.load(f)

    return_messages = []
    import_dates_list = []
    for date in import_dates:
        import_dates_list.append(date)
    if target_start_date and target_end_date:
        move_start = import_dates_list.index(move_target_start_date)
        move_end = import_dates_list.index(move_target_end_date) + 1
        move_dates = import_dates_list[move_start:move_end]

        for date in move_dates:
            current_title  = import_dates[move_source_start_date][event]['title']
            import_dates[date][event]['title'] = current_title
            import_dates[date][event]['start date'] = move_target_start_date
            import_dates[date][event]['end date'] = move_target_end_date
            if location:
                import_dates[date][event]['location'] = location
            elif not location:
                current_location = import_dates[move_source_start_date][event]['location']
                import_dates[date][event]['location'] = current_location
            if note:
                import_dates[date][event]['note'] = note
            elif not note:
                current_note = import_dates[move_source_start_date][event]['note']
                import_dates[date][event]['note'] = current_note

        message_0 = f"{event} has been moved from old dates to {move_dates}."
        return_messages.append(message_0)
        if location:
            message_1 = f"location of {event} has been changed to {location}."
            return_messages.append(message_1)
        if note:
            message_2 = f"note of {event} has been changed to {note}."
            return_messages.append(message_2)

    elif not target_start_date and not target_end_date:
        move_start = import_dates_list.index(move_source_start_date)
        move_end = import_dates_list.index(move_source_end_date) + 1
        move_dates = import_dates_list[move_start:move_end]

        for date in move_dates:
            if location:
                import_dates[date][event]['location'] = location
            if note:
                import_dates[date][event]['note'] = note
        
        if location:
            message_0 = f"location of {event} has been changed to {location}."
            return_messages.append(message_0)
        if note:
            message_1 = f"note of {event} has been changed to {note}."
            return_messages.append(message_1)

    with open(filename, 'w') as f:
        json.dump(import_dates, f, indent=4)
    message = f"{event} has been moved from {move_source_start_date} to"
    message += f" {move_target_start_date}"
    return_messages.append(message)
    return return_messages
