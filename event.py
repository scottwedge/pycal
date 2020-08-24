'''This module contains Event class that represents single event in calendar.'''

class Calendar():
    '''Representation of a calendar.'''

    def __init__(self, name):
        '''Initialize attributes.'''
        self.name = name
        self.events = []
        self.count = 0

    def __len__(self):
        '''Return a length of self.events.'''
        return len(self.events)

    def __getitem__(self, i):
        '''Return given event.'''
        if i in range(len(self.events)):
            return self.events.__getitem__(i)
        elif i not in range(len(self.events)):
            raise IndexError

    def __contains__(self, item):
        '''Membership test.'''
        if item in self.events:
            return True
        elif item not in self.events:
            return False

    def __iter__(self):
        '''Create an iterator.'''
        return self

    def __next__(self):
        '''Access one event at a time.'''
        if self.count == len(self.events):
            self.count = 0
            raise StopIteration
        return_event = self.events,__getitem__(count)
        self.count += 1
        return return_event

class Event():
    '''Representation of a single calendar event.'''

    def create_id(self):
        '''Create ID number for an event.'''

    def __init__(self, title, start_date, end_date=None,
                 location=None, note=None):
        '''Initialize attributes.'''
        self.instance_variables = {}
        self.title = title
        self.instance_variables['title'] = self.title
        self.start_date = start_date
        self.instance_variables['start_date'] = self.start_date
        self.end_date = end_date
        self.instance_variables['end_date'] = self.end_date
        self.location = location
        self.instance_variables['location'] = self.location
        self.note = note
        self.instance_variables['note'] = self.note
        self.id = ''
        # self.instance_variables.append(self.id)
        self.keys = []
        self.values = []
        self.count = 0
        for key, value in self.instance_variables.items():
            self.keys.append(key)
            self.values.append(value)
        self.index = len(self.keys)


    def __len__(self):
        '''Return length of an event - number of attributes.'''
        length_list = []
        for item in self.instance_variables:
            length_list.append(item)
        return len(length_list)

    def display_attributes(self, *attributes):
        '''Display specified attribute(s).'''
        for attribute in attributes:
            print(self.attribute)

    def __getitem__(self, key):
        '''Return given attribute.'''
        if key in self.instance_variables.keys():
            return self.instance_variables[key]
        elif key not in self.instance_variables:
            raise KeyError

    def __setitem__(self, key, value):
        '''Set given attribute.'''
        self.instance_variables[key] = value
        self.key = value

    def __contains__(self, item):
        '''Membership test.'''
        if item in self.instance_variables:
            return True
        elif item not in self.instance_variables:
            return False

    def __iter__(self):
        '''Create an iterator.'''
        return self

    def __next__(self) -> list:
        '''Access one attribute at a time.'''

        '''It returns list that cotains name of the attribute and
        its value.'''
        self.return_list = []
        if self.count == self.index:
            self.count = 0
            raise StopIteration
        self.return_list.append(self.keys[self.count])
        self.return_list.append(self.values[self.count])
        self.count += 1
        return self.return_list

