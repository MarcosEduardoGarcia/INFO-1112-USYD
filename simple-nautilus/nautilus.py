#!/usr/bin/env python3

# Marcos Eduardo Garcia Ortiz
# Student id: 520605309
# 28-09-2022
# USYD

class File:
    '''
    A class used to represent a File

    ...

    Attributes
    ----------
    type_file : str
        type of file bit
    perms_ow : list
        list with permission bits for the owner
    perms_ot : list
        list with permission bits for the others
    name : str
        name of the file
    user : str
        user that create the file

    Methods
    -------
    properties():
        Extract the properties of a file object and create a
        formatted string to print out in a format similar to
        linux e.g rwxrwx user name

    basic_properties():
        Extract the name of the object in a string

    def del_all():
        set all the items to '-' in perms_ow and perms_ot

    def add_all():
        set the items in perms_ow and perms_ot to r w x in that order

    def add_all_ow():
        set the items in perms_ow to r w x in that order

    def add_all_ot():
        set the items in perms_ot to r w x in that order

    def del_all_ow():
        set all the items to '-' in perms_ow

    def del_all_ot():
        set all the items to '-' in perms_ot

    read_only_ow():
        Change perms_ow to ['r', '-', '-']
    write_only_ow():
        Change perms_ow to ['-', 'w', '-']
    exec_only_ow():
        Change perms_ow to ['-', '-', 'x']

    read_only_ot():
        Change perms_ot to ['r', '-', '-']
    write_only_ot():
        Change perms_ot to ['-', 'w', '-']
    exec_only_ot():
        Change perms_ot to ['-', '-', 'x']

    add_read_ow():
        Change perms_ow[0] to 'r'
    add_write_ow():
        Change perms_ow[1] to 'w'
    add_exec_ow():
        Change perms_ow[2] to 'x'

    del_read_ow():
        Change perms_ow[0] to '-'
    del_write_ow():
        Change perms_ow[1] to '-'
    del_exec_ow():
        Change perms_ow[2] to '-'

    add_read_ot():
        Change perms_ot[0] to 'r'
    add_write_ot():
        Change perms_ot[1] to 'w'
    add_exec_ot():
        self.perms_ot[2] to 'x'

    del_read_ot():
        Change perms_ot[0] to '-'
    del_write_ot():
        Change perms_ot[1] to '-'
    del_exec_ot():
        Change perms_ot[2] to '-'
    '''

    type_file = '-'
    perms_ow = ['r', 'w', '-']
    perms_ot = ['r', '-', '-']

    def __init__(self, name, user):
        '''
        Constructs all the necessary attributes for the file object

        Parameters
        ----------
            name : str
                the  name of the file
            user : str
                the name of user that create the file
        '''
        self.name = name
        self.user = user

    def get_type(self): return self.type_file
    def set_type(self, type_file): self.type_file = type_file

    def get_row(self): return self.perms_ow[0]
    def get_wow(self): return self.perms_ow[1]
    def get_xow(self): return self.perms_ow[2]

    def get_rot(self): return self.perms_ot[0]
    def get_wot(self): return self.perms_ot[1]
    def get_xot(self): return self.perms_ot[2]

    def get_name(self): return self.name
    def get_user(self): return self.user

    def set_name(self, name): self.name = name
    def set_user(self, user): self.user = user

    def properties(self):
        prop = (self.type_file + self.perms_ow[0] + self.perms_ow[1]
                + self.perms_ow[2] + self.perms_ot[0] + self.perms_ot[1]
                + self.perms_ot[2] + ' ' + self.user + ' ' + self.name)
        return prop

    def basic_properties(self):
        prop = self.name
        return prop

    def del_all(self):
        self.perms_ow = ['-', '-', '-']
        self.perms_ot = ['-', '-', '-']

    def add_all(self):
        self.perms_ow = ['r', 'w', 'x']
        self.perms_ot = ['r', 'w', 'x']

    def add_all_ow(self):
        self.perms_ow = ['r', 'w', 'x']

    def add_all_ot(self):
        self.perms_ot = ['r', 'w', 'x']

    def del_all_ow(self):
        self.perms_ow = ['-', '-', '-']

    def del_all_ot(self):
        self.perms_ot = ['-', '-', '-']

    def read_only_ow(self): self.perms_ow = ['r', '-', '-']
    def write_only_ow(self): self.perms_ow = ['-', 'w', '-']
    def exec_only_ow(self): self.perms_ow = ['-', '-', 'x']

    def read_only_ot(self): self.perms_ot = ['r', '-', '-']
    def write_only_ot(self): self.perms_ot = ['-', 'w', '-']
    def exec_only_ot(self): self.perms_ot = ['-', '-', 'x']

    def add_read_ow(self): self.perms_ow[0] = 'r'
    def add_write_ow(self): self.perms_ow[1] = 'w'
    def add_exec_ow(self): self.perms_ow[2] = 'x'

    def del_read_ow(self): self.perms_ow[0] = '-'
    def del_write_ow(self): self.perms_ow[1] = '-'
    def del_exec_ow(self): self.perms_ow[2] = '-'

    def add_read_ot(self): self.perms_ot[0] = 'r'
    def add_write_ot(self): self.perms_ot[1] = 'w'
    def add_exec_ot(self): self.perms_ot[2] = 'x'

    def del_read_ot(self): self.perms_ot[0] = '-'
    def del_write_ot(self): self.perms_ot[1] = '-'
    def del_exec_ot(self): self.perms_ot[2] = '-'

    def __repr__(self):
        return str(self.name)


class Folder(File):
    '''
    A class used to represent Folder object 
    This is a children class from file that
    only change the attributes of the object
    '''

    type_file = 'd'
    perms_ow = ['r', 'w', 'x']
    perms_ot = ['r', '-', 'x']


class User:
    '''
    A class used to represent a User

    ...

    Attributes
    ----------
    name : str
        name of the user

    Methods
    -------
    get_name():
        Return the name of the user
    '''

    def __init__(self, name):
        '''
        COnstructs all the necesary attributes for the user object

        Parameters
        ----------
            name : str
                the name of user
        '''

        self.name = name

    def get_name(self): return self.name

    def __repr__(self): return str(self.name)


class Terminal:
    '''
    A class to represent the virtual bash 

    ...

    Attributes
    ----------
    None

    Methods
    -------
    def pwd_command(self, command, cur_path):
        Prints the current path
    mkdir_command(self, command, cur_dir):
        Creates new directories
    touch_command(self, command, cur_dir):
        Creates new files
    cd_command(self, command, cur_dir, cur_path):
        Enter to a directory
    cd_enter_out(self, result, cur_dir, cur_path):
        Auxiliary function to enter directories
    copy_command(self, command, cur_dir):
        Copy a file to other location
    determinant_source(self, result, aux1):
        Auxiliary function of copy to get the soruce file
    determinant_dest(self, result, aux1):
        Auxiliary function of copy to get the destination
    move_command(self, command, cur_dir):
        Move one file to other location
    determinant_source_mv(self, result, aux1):
        Auxiliary function of move to get the soruce file
    determinant_dest_mv(self, result, aux1):
        Auxiliary function of move to get the destination
    remove_command(self, command, cur_dir):
        Remove a file
    removeDir_command(self, command, cur_dir):
        Remove an empty directory
    adduser_command(self, command, user_list, current_user):
        Add a new user to the terminal
    delususer_command(self, command, user_list, current_user):
        Delete users from the terminal
    su_command(self, command, user_list, current_user):
        Change the current user of the terminal
    ls_command(self, command, cur_dir):
        list the files
    chmod_command(self, command, cur_dir):
        change the permissions bits in files
    determinant_object(self, result, aux):
        Auxiliary function of chmod to get the file
    change_perms(self, result, file):
        Auxiliary function of chmod to get the permissions
    chown_command(self, command, cur_dir, user_list, current_user):
        Change the user of the file
    analize_perms(self, string):
        Analize the permissions parameter
    ls_full(self, aux):
        list all the files in one directory
    ls_name(self, aux):
        list all names in one directory
    ls_full_dot(self, aux):
        list all name including the dot files
    analize_string(self, string):
        Analyze the complete string to determine paths and commands 
    analize_symbols(self, string):
        Filter the forbiden symbols
    split_quotes(self, string):
        Split the paths that have quotes

    '''

    def __init__(self):
        '''
        Create all the necessary elements to run the simple Nautilus
        '''
        self.root_user = User('root')
        self.users = []
        self.users.append(self.root_user)

        # Creating root folder
        self.root = {}
        self.root_folder = Folder('/', self.root_user.get_name())

        self.root[self.root_folder] = {}
        self.root_bin = self.root

        object_keys = list(self.root.keys())
        self.root = self.root[object_keys[0]]

        # When the program starts
        self.cur_dir = self.root
        self.cur_path = '/'
        self.cur_terminaluser = self.root_user

        while True:
            # Display the terminal
            promt = (self.cur_terminaluser.get_name() + ':' + self.cur_path + '$ ')
            # Receive comman string
            command = input(str(promt))
            command = command.strip()
            validation = self.analize_symbols(command)

            if command.isspace():
                continue
            if command:
                if '"' in command:
                    command = self.split_quotes(command)

                else:
                    command = command.split()
            else:
                continue

            if validation is False:
                print(command[0] + ': Invalid syntax')
                continue
            else:
                pass

            # Commands
            if command[0] == 'mkdir':
                self.mkdir_command(command, self.cur_dir)

            elif command[0] == 'touch':
                self.touch_command(command, self.cur_dir)

            elif command[0] == 'cd':
                self.cd_command(command, self.cur_dir, self.cur_path)
                if len(self.cur_path) > 1:
                    if self.cur_path[0] == '/' and self.cur_path[1] == '/':
                        self.cur_path = self.cur_path[1:]

            elif command[0] == 'pwd':
                self.pwd_command(command, self.cur_path)

            elif command[0] == 'cp':
                self.copy_command(command, self.cur_dir)

            elif command[0] == 'mv':
                self.move_command(command, self.cur_dir)

            elif command[0] == 'rm':
                self.remove_command(command, self.cur_dir)

            elif command[0] == 'rmdir':
                self.removeDir_command(command, self.cur_dir)

            elif command[0] == 'adduser':
                self.adduser_command(command, self.users, self.cur_terminaluser)

            elif command[0] == 'deluser':
                self.delususer_command(command, self.users, self.cur_terminaluser)

            elif command[0] == 'su':
                self.su_command(command, self.users, self.cur_terminaluser)

            elif command[0] == 'ls':
                self.ls_command(command, self.cur_dir)

            elif command[0] == 'chmod':
                self.chmod_command(command, self.cur_dir)

            elif command[0] == 'chown':
                self.chown_command(command, self.cur_dir, self.users, self.cur_terminaluser)

            elif command[0] == 'xd':
                print(self.root_bin)

            elif command[0] == 'exit':
                if len(command) > 1:
                    print('exit: Invalid syntax')
                else:
                    print('bye,', self.cur_terminaluser.get_name())
                    exit()
            else:
                print(command[0] + ': Command not found')

    def pwd_command(self, command, cur_path):
        '''
        Prints the current path

        Parameters
        ----------
        command : list
            The command entered by user splitted in a list
        cur_path : str
            The current path of the Terminal
        Returns
        -------
        None
        '''

        if len(command) == 1:
            print(cur_path)
        else:
            print('pwd: Invalid syntax')

    def mkdir_command(self, command, cur_dir):
        '''
        Creates new directories and prints the errors in terminal
        if a path was given in the command[1] the function will 
        loop through the dictionary cur_dir to find the path and
        verifying the type (folder or file) and create the directory if
        is possible

        Parameters
        ----------
        command : list
            The command entered by user splitted in a list
        cur_dir : dictionary
            The main dictionary where the objects will be created or 
            the start point to enter in other dictionaries in case of a path

        Returns
        -------
        None
        '''

        if len(command) == 1:
            print('mkdir: Invalid syntax')
        elif len(command) == 2:
            result = self.analize_string(command[1])
            counter = 0

            if command[1][0] == '/' and len(command[1]) > 1:
                aux = self.root
            else:
                aux = cur_dir
            cur_path = self.cur_path
            for i in range(len(result)):
                keys = list(aux.keys())
                keys = [str(x) for x in keys]
                object_keys = list(aux.keys())

                if result[i] in keys:
                    indice = keys.index(result[i])
                    if object_keys[indice].get_type() == 'd':
                        aux = aux[object_keys[indice]]
                    else:
                        print('mkdir: File exists')
                        break
                    counter += 1
                elif result[i] not in keys and i == len(result)-1:
                    self.folder = Folder(result[i], self.cur_terminaluser.get_name())
                    aux[self.folder] = {}

                elif result[i] == '.':
                    pass

                elif result[i] == '..':
                    slashes = [pos for pos, char in enumerate(cur_path) if char == '/']
                    if len(slashes) == 1 :
                        cur_path = '/'
                        pass
                    else:
                        # Get the path before last slash
                        cur_path = cur_path[:max(slashes)]
                    if cur_path == '/':
                        aux = self.root_bin
                        result_analize = ['/']
                    else:
                        aux = self.root
                        result_analize = self.analize_string(cur_path)

                    if isinstance(result_analize, list):
                        for i in range(len(result_analize)):
                            keys = list(aux.keys())
                            keys = [str(x) for x in keys]
                            object_keys = list(aux.keys())
                            if result_analize[i] in keys:
                                indice = keys.index(result_analize[i])
                                aux = aux[object_keys[indice]]

                else:
                    print('mkdir: Ancestor directory does not exist')
                    break
            if counter == len(result):
                print('mkdir: File exists')
        elif len(command) == 3:
            if command[1] == '-p':
                result = self.analize_string(command[2])
                if command[2][0] == '/' and len(command[2]) > 1:
                    aux = self.root
                else:
                    aux = cur_dir
                cur_path = self.cur_path
                for i in range(len(result)):
                    keys = list(aux.keys())
                    keys = [str(x) for x in keys]
                    object_keys = list(aux.keys())
                    if result[i] in keys:
                        indice = keys.index(result[i])

                        if object_keys[indice].get_type() == 'd':
                            aux = aux[object_keys[indice]]
                        elif object_keys[indice].get_type() == '-':
                            break
                        else:
                            self.folder = Folder(result[i], self.cur_terminaluser.get_name())
                            aux[self.folder] = {}
                            aux = aux[self.folder]

                    elif result[i] == '.':
                        pass

                    elif result[i] == '..':
                        slashes = [pos for pos, char in enumerate(cur_path) if char == '/']
                        if len(slashes) == 1 :
                            cur_path = '/'
                            pass
                        else:
                            # Imprime el path hasta antes de la ultima slash
                            cur_path = cur_path[:max(slashes)]
                        if cur_path == '/':
                            aux = self.root_bin
                            result_analize = ['/']
                        else:
                            aux = self.root
                            result_analize = self.analize_string(cur_path)

                        if isinstance(result_analize, list):
                            for i in range(len(result_analize)):
                                keys = list(aux.keys())
                                keys = [str(x) for x in keys]
                                object_keys = list(aux.keys())
                                if result_analize[i] in keys:
                                    indice = keys.index(result_analize[i])
                                    aux = aux[object_keys[indice]]

                    else:
                        self.folder = Folder(result[i], self.cur_terminaluser.get_name())
                        aux[self.folder] = {}
                        aux = aux[self.folder]
            else:
                print('mkdir: Invalid syntax')

    def touch_command(self, command, cur_dir):
        '''
        Creates new files and prints the errors in terminal
        if a path was given in the command[1] the function will 
        loop through the dictionary cur_dir to find the path and
        verifying the type (folder or file) and create the file if
        is possible

        Parameters
        ----------
        command : list
            The command entered by user splitted in a list
        cur_dir : dictionary
            The main dictionary where the objects will be created or 
            the start point to enter in other dictionaries in case of a path

        Returns
        -------
        None
        '''

        if len(command) == 1:
            print('touch: Invalid syntax')
        elif len(command) == 2:
            result = self.analize_string(command[1])

            if command[1][0] == '/' and len(command[1]) > 1:
                aux = self.root
            else:
                aux = cur_dir

            cur_path = self.cur_path
            for i in range(len(result)):
                keys = list(aux.keys())
                keys = [str(x) for x in keys]
                object_keys = list(aux.keys())
                if result[i] in keys:
                    indice = keys.index(result[i])
                    if i == len(result) - 1:
                        if object_keys[indice].get_type() == 'd':
                            aux = aux[object_keys[indice]]
                        elif object_keys[indice].get_type() == '-':
                            break
                        else:
                            pass
                    else:
                        if object_keys[indice].get_type() == 'd':
                            aux = aux[object_keys[indice]]
                        else:
                            print('touch: Ancestor directory does not exist')
                            break
                elif i == len(result) - 1 and result[i] not in keys:
                    self.file = File(result[i], self.cur_terminaluser.get_name())
                    aux[self.file] = None

                elif result[i] == '.':
                    pass

                elif result[i] == '..':
                    slashes = [pos for pos, char in enumerate(cur_path) if char == '/']
                    if len(slashes) == 1 :
                        cur_path = '/'
                        pass
                    else:
                        # Imprime el path hasta antes de la ultima slash
                        cur_path = cur_path[:max(slashes)]
                    if cur_path == '/':
                        aux = self.root_bin
                        result_analize = ['/']
                    else:
                        aux = self.root
                        result_analize = self.analize_string(cur_path)

                    if isinstance(result_analize, list):
                        for i in range(len(result_analize)):
                            keys = list(aux.keys())
                            keys = [str(x) for x in keys]
                            object_keys = list(aux.keys())
                            if result_analize[i] in keys:
                                indice = keys.index(result_analize[i])
                                aux = aux[object_keys[indice]]

                else:
                    print('touch: Ancestor directory does not exist')
                    break
        else:
            print('touch: Invalid syntax')

    def cd_command(self, command, cur_dir, cur_path):
        '''
        Change the current directory (dictionary) in the terminal

        Parameters
        ----------
        command : list
            The command entered by user splitted in a list
        cur_dir : dictionary
            The current dictionary to start enter in other directories
        cur_path : string
            The current path displayed in the terminal that will changes 
            based in which directory the user enters

        Returns
        -------
        None
        '''

        if len(command) == 1:
            print('cd: Invalid syntax')
        elif len(command) == 2:
            if command[1] == '/':
                self.cur_path = '/'
                self.cur_dir = self.root
                return
            if command[1][0] == '/' and len(command[1]) > 1:
                # Absolute path
                self.cur_dir = self.root
                self.cur_path = '/'
            result = self.analize_string(command[1])
            if result[0] == '':
                del result[0]
            dir_inicial = cur_dir
            path_inicial = cur_path
            for i in range(len(result)):
                a = self.cd_enter_out(result[i], self.cur_dir, self.cur_path)
                if a == 1:
                    print('cd: No such file or directory')
                    self.cur_dir = dir_inicial
                    self.cur_path = path_inicial
                    break
                elif a == 2:
                    print('cd: Destination is a file')
                    self.cur_dir = dir_inicial
                    self.cur_path = path_inicial
                    break
        else:
            print('cd: Invalid syntax')

    def cd_enter_out(self, result, cur_dir, cur_path):
        '''
        Auxiliary function to enter in the directories

        Parameters
        ----------
        result : string
            The directory that will be analysed if exists the
            current dictionary will change 
        cur_dir : dictionary
            The dictionary that contain the objects of folders
            and files
        cur_path : string
            The current path displayed in terminal that will be chaged
            based on which directory enters
        
        Returns
        -------
        flags : int
            Based on whether or not the directory is found,
            certain useful flags are returned to determine errors.
        '''

        keys = list(cur_dir.keys())
        keys = [str(x) for x in keys]
        object_keys = list(cur_dir.keys())
        if result in keys:
            indice = keys.index(result)
            if object_keys[indice].get_type() == 'd':
                cur_dir = cur_dir[object_keys[indice]]
                cur_path = cur_path + '/' + result
                self.cur_dir = cur_dir
                self.cur_path = cur_path
            else:
                flag = 2
                return flag
        elif result == '..':
            slashes = [pos for pos, char in enumerate(cur_path) if char == '/']
            if len(slashes) == 1:
                cur_path = '/'
            else:
                # Imprime el path hasta antes de la ultima slash
                cur_path = cur_path[:max(slashes)]
            self.cur_path = cur_path
            if cur_path == '/':
                aux = self.root_bin
                result = ['/']
            else:
                aux = self.root
                result = self.analize_string(cur_path)
                #result = result[2:]
            if isinstance(result, list):
                for i in range(len(result)):
                    keys = list(aux.keys())
                    keys = [str(x) for x in keys]
                    object_keys = list(aux.keys())
                    if result[i] in keys:
                        indice = keys.index(result[i])
                        aux = aux[object_keys[indice]]
                        self.cur_dir = aux
        elif result == '.':
            pass
        else:
            flag = 1
            return flag

    def copy_command(self, command, cur_dir):
        '''
        Create a copy of one file in the current location
        or another and prints errors

        Parameters
        ----------

        command : list 
            The command entered by user splitted in a list
        cur_dir : dictionary
            The current dictionary to start the traversal
            to locate the file and copy in other location

        Returns
        -------
        None
        '''

        self.objeto = 0
        self.destino = 0
        self.name = ''

        if len(command) < 3:
            print('cp: Invalid syntax')
            return

        if len(command) > 3:
            print('cp: Invalid syntax')
            return

        if command[1][0] == '/' and len(command[1]) > 1:
            aux1 = self.root
        else:
            aux1 = cur_dir

        if command[2][0] == '/' and len(command[2]) > 1:
            aux2 = self.root
        else:
            aux2 = cur_dir

        result = self.analize_string(command[1])
        a = self.determinant_source(result, aux1)
        result2 = self.analize_string(command[2])
        b = self.determinant_dest(result2, aux2)

        # a = 1 file source exist
        # a = 2 file is a directory

        # b = 1 file dest exist
        # b = 2 file dont exist and create
        # b = 3 file is a directory
        if a == 1 and b == 1:
            print('cp: File exists')
        elif a == 1 and b == 2:
            # Crear un nuevo objeto
            self.copy_file = Folder(self.name, self.objeto.get_user())
            self.copy_file.type_file = self.objeto.get_type()
            self.copy_file.read_ow = self.objeto.get_row()
            self.copy_file.write_ow = self.objeto.get_wow()
            self.copy_file.execute_ow = self.objeto.get_xow()

            self.copy_file.read_ot = self.objeto.get_rot()
            self.copy_file.write_ot = self.objeto.get_wot()
            self.copy_file.execute_ot = self.objeto.get_xot()
            self.destino[self.copy_file] = None
        elif a == 1 and b == 3:
            print('cp: Destination is a directory')
        elif a == 2 and b == 1:
            print('cp: Source is a directory')
        elif a == 2 and b == 2:
            print('cp: Source is a directory')
        elif a == 2 and b == 3:
            print('cp: Destination is a directory')
        elif a == 4:
            print('cp: No such file')
        elif a == 1 and b == 4:
            print('cp: No such file or directory')

    def determinant_source(self, result, aux1):
        '''
        Determine if the object to copy is a file and save
        the object in a variable

        Parameters
        ----------
        result : list
            source path segmented into a list
        aux1: dictionary
            start dictionary to search the file

        Returns
        -------
        flag : int
            Based on whether or not the file is found,
            certain useful flags are returned to determine errors.
        '''
        cur_path = self.cur_path
        for i in range(len(result)):
            keys = list(aux1.keys())
            keys = [str(x) for x in keys]
            object_keys = list(aux1.keys())

            if result[i] in keys:
                indice = keys.index(result[i])
                if i == len(result) - 1:
                    if object_keys[indice].get_type() == 'd':
                        flag = 2
                        return flag
                    else:
                        flag = 1
                        self.objeto = object_keys[indice]
                        return flag
                else:
                    if object_keys[indice].get_type() == 'd':
                        aux1 = aux1[object_keys[indice]]
                    else:
                        flag = 4
                        return flag

            elif result[i] == '.':
                pass

            elif result[i] == '..':
                slashes = [pos for pos, char in enumerate(cur_path) if char == '/']
                if len(slashes) == 1:
                    cur_path = '/'
                    pass
                else:
                    # Imprime el path hasta antes de la ultima slash
                    cur_path = cur_path[:max(slashes)]

                if cur_path == '/':
                    aux1 = self.root_bin
                    result_analize = ['/']
                else:
                    aux1 = self.root
                    result_analize = self.analize_string(cur_path)

                if isinstance(result_analize, list):
                    for i in range(len(result_analize)):
                        keys = list(aux1.keys())
                        keys = [str(x) for x in keys]
                        object_keys = list(aux1.keys())
                        if result_analize[i] in keys:
                            indice = keys.index(result_analize[i])
                            aux1 = aux1[object_keys[indice]]
            else:
                # En algun punto la ruta no existio
                flag = 4
                return flag

    def determinant_dest(self, result, aux1):
        '''
        Determine if in the location there is no a
        file called with the same name and verify that 
        the path is valid

        Parameters
        ----------
        result : list
            destination path segmented into a list
        aux1: dictionary
            start dictionary to search the file

        Returns
        -------
        flag : int
            Based on whether or not the file is found,
            certain useful flags are returned to determine errors.
        '''
        cur_path = self.cur_path
        for i in range(len(result)):
            keys = list(aux1.keys())
            keys = [str(x) for x in keys]
            object_keys = list(aux1.keys())
            if result[i] in keys:
                indice = keys.index(result[i])
                if i == len(result) - 1:
                    if object_keys[indice].get_type() == 'd':
                        flag = 3
                        return flag
                    else:
                        flag = 1
                        return flag
                else:
                    if object_keys[indice].get_type() == 'd':
                        aux1 = aux1[object_keys[indice]]
                    else:
                        flag = 4
                        return flag
            elif result[i] not in keys and i == len(result)-1:
                flag = 2
                self.destino = aux1
                self.name = result[i]
                return flag

            elif result[i] == '.':
                pass
            elif result[i] == '..':
                slashes = [pos for pos, char in enumerate(cur_path) if char == '/']
                if len(slashes) == 1:
                    cur_path = '/'
                    pass
                else:
                    # Imprime el path hasta antes de la ultima slash
                    cur_path = cur_path[:max(slashes)]

                if cur_path == '/':
                    aux1 = self.root_bin
                    result_analize = ['/']
                else:
                    aux1 = self.root
                    result_analize = self.analize_string(cur_path)

                if isinstance(result_analize, list):
                    for i in range(len(result_analize)):
                        keys = list(aux1.keys())
                        keys = [str(x) for x in keys]
                        object_keys = list(aux1.keys())
                        if result_analize[i] in keys:
                            indice = keys.index(result_analize[i])
                            aux1 = aux1[object_keys[indice]]
            else:
                # En algun punto la ruta no existio
                flag = 4
                return flag

    def move_command(self, command, cur_dir):
        '''
        Move one file to other location and prints in case of errors

        Parameters
        ----------

        command : list 
            The command entered by user splitted in a list
            where the soruce and destination is.
        cur_dir : dictionary
            The current dictionary to start the traversal
            to locate the file and copy in other location

        Returns
        -------
        None
        '''

        self.objeto = 0
        self.destino = 0
        self.original_source = 0
        self.name = ''

        if len(command) < 3 or len(command) > 3:
            print('mv: Invalid syntax')
            return
        # Analize path 1 path y termina con file

        if command[1][0] == '/' and len(command[1]) > 1:
            aux1 = self.root
        else:
            aux1 = cur_dir

        if command[2][0] == '/' and len(command[2]) > 1:
            aux2 = self.root
        else:
            aux2 = cur_dir

        result = self.analize_string(command[1])
        a = self.determinant_source_mv(result, aux1)
        result2 = self.analize_string(command[2])
        b = self.determinant_dest_mv(result2, aux2)

        #  = 1 Directory
        # a = 2 File exist can move
        # a = 3 No file to move

        # b = 1 Directory
        # b = 2 A file exist
        # b = 3 No file
        # b = 4 Can move and create

        if a == 1 and (b == 2 or b == 3 or b == 4):
            print('mv: Source is a directory')
        elif a == 2 and b == 1:
            print('mv: Destination is a directory')
            # Recreate object
            self.move_file = File(self.objeto.get_name(), self.objeto.get_user())
            self.move_file.type_file = self.objeto.get_type()
            self.move_file.read_ow = self.objeto.get_row()
            self.move_file.write_ow = self.objeto.get_wow()
            self.move_file.execute_ow = self.objeto.get_xow()

            self.move_file.read_ot = self.objeto.get_rot()
            self.move_file.write_ot = self.objeto.get_wot()
            self.move_file.execute_ot = self.objeto.get_xot()
            self.original_source[self.move_file] = None

        elif a == 2 and b == 2:
            print('mv: File exists')
            # Recreate object
            self.move_file = File(self.objeto.get_name(), self.objeto.get_user())
            self.move_file.type_file = self.objeto.get_type()
            self.move_file.read_ow = self.objeto.get_row()
            self.move_file.write_ow = self.objeto.get_wow()
            self.move_file.execute_ow = self.objeto.get_xow()

            self.move_file.read_ot = self.objeto.get_rot()
            self.move_file.write_ot = self.objeto.get_wot()
            self.move_file.execute_ot = self.objeto.get_xot()
            self.original_source[self.move_file] = None

        elif a == 2 and b == 3:
            print('mv: No such file or directory')
            # Recreate object
            self.move_file = File(self.objeto.get_name(), self.objeto.get_user())
            self.move_file.type_file = self.objeto.get_type()
            self.move_file.read_ow = self.objeto.get_row()
            self.move_file.write_ow = self.objeto.get_wow()
            self.move_file.execute_ow = self.objeto.get_xow()

            self.move_file.read_ot = self.objeto.get_rot()
            self.move_file.write_ot = self.objeto.get_wot()
            self.move_file.execute_ot = self.objeto.get_xot()
            self.original_source[self.move_file] = None

        elif a == 2 and b == 4:
            self.move_file = File(self.name, self.objeto.get_user())
            self.move_file.type_file = self.objeto.get_type()
            self.move_file.read_ow = self.objeto.get_row()
            self.move_file.write_ow = self.objeto.get_wow()
            self.move_file.execute_ow = self.objeto.get_xow()

            self.move_file.read_ot = self.objeto.get_rot()
            self.move_file.write_ot = self.objeto.get_wot()
            self.move_file.execute_ot = self.objeto.get_xot()

            self.destino[self.move_file] = None

        elif a == 3:
            print('mv: No such file')

        elif a == 1 and b == 1:
            print('mv: Destination is a directory')

    def determinant_source_mv(self, result, aux1):
        '''
        Determine if the object to move is a file and save
        the object in a variable and delete from the directory

        Parameters
        ----------
        result : list
            source path segmented into a list
        aux1: dictionary
            start dictionary to search the file

        Returns
        -------
        flag : int
            Based on whether or not the file is found,
            certain useful flags are returned to determine errors.
        '''
        cur_path = self.cur_path
        for i in range(len(result)):
            keys = list(aux1.keys())
            keys = [str(x) for x in keys]
            object_keys = list(aux1.keys())

            if result[i] in keys:
                indice = keys.index(result[i])
                if i == len(result) - 1:
                    if object_keys[indice].get_type() == 'd':
                        flag = 1
                        return flag
                    else:
                        self.objeto = object_keys[indice]
                        del aux1[object_keys[indice]]
                        self.original_source = aux1
                        flag = 2
                        return flag
                else:
                    if object_keys[indice].get_type() == 'd':
                        aux1 = aux1[object_keys[indice]]
                    else:
                        flag = 3
                        return flag

            elif result[i] == '.':
                pass

            elif result[i] == '..':
                slashes = [pos for pos, char in enumerate(cur_path) if char == '/']

                if len(slashes) == 1:
                    cur_path = '/'
                    pass
                else:
                    # Imprime el path hasta antes de la ultima slash
                    cur_path = cur_path[:max(slashes)]

                if cur_path == '/':
                    aux1 = self.root_bin
                    result_analize = ['/']
                else:
                    aux1 = self.root
                    result_analize = self.analize_string(cur_path)

                if isinstance(result_analize, list):
                    for i in range(len(result_analize)):
                        keys = list(aux1.keys())
                        keys = [str(x) for x in keys]
                        object_keys = list(aux1.keys())
                        if result_analize[i] in keys:
                            indice = keys.index(result_analize[i])
                            aux1 = aux1[object_keys[indice]]

            else:
                # En algun punto la ruta no existio
                flag = 3
                return flag

    def determinant_dest_mv(self, result, aux1):
        '''
        Determine if in the location there is no a
        file called with the same name and verify that 
        the path is valid

        Parameters
        ----------
        result : list
            destination path segmented into a list
        aux1: dictionary
            start dictionary to search the file

        Returns
        -------
        flag : int
            Based on whether or not the file is found,
            certain useful flags are returned to determine errors.
        '''
        cur_path = self.cur_path
        for i in range(len(result)):
            keys = list(aux1.keys())
            keys = [str(x) for x in keys]
            object_keys = list(aux1.keys())
            if result[i] in keys:
                indice = keys.index(result[i])
                if i == len(result) - 1:
                    if object_keys[indice].get_type() == 'd':
                        flag = 1
                        return flag
                    else:
                        flag = 2
                        return flag
                else:
                    if object_keys[indice].get_type() == 'd':
                        aux1 = aux1[object_keys[indice]]
                    else:
                        flag = 3
                        return flag

            elif result[i] not in keys and i == len(result)-1:
                flag = 4
                self.destino = aux1
                self.name = result[i]
                return flag

            elif result[i] == '.':
                pass

            elif result[i] == '..':
                slashes = [pos for pos, char in enumerate(cur_path) if char == '/']
                if len(slashes) == 1:
                    cur_path = '/'
                    pass
                else:
                    # Imprime el path hasta antes de la ultima slash
                    cur_path = cur_path[:max(slashes)]

                if cur_path == '/':
                    aux1 = self.root_bin
                    result_analize = ['/']
                else:
                    aux1 = self.root
                    result_analize = self.analize_string(cur_path)

                if isinstance(result_analize, list):
                    for i in range(len(result_analize)):
                        keys = list(aux1.keys())
                        keys = [str(x) for x in keys]
                        object_keys = list(aux1.keys())
                        if result_analize[i] in keys:
                            indice = keys.index(result_analize[i])
                            aux1 = aux1[object_keys[indice]]

            else:
                # En algun punto la ruta no existio
                flag = 3
                return flag

    def remove_command(self, command, cur_dir):
        '''
        Remove a file from a directory

        Parameters
        ----------
        command : list
            The command entered by user splitted in a list
            that could be a path or name of file
        cur_dir : dictionary
            start dictionary to search the file and delete it
        '''

        if len(command) == 1 or len(command) > 2:
            print('rm: Invalid syntax')
        elif len(command) == 2:
            result = self.analize_string(command[1])
            cur_path = self.cur_path
            if command[1][0] == '/' and len(command[1]) > 1:
                aux = self.root
            else:
                aux = cur_dir

            for i in range(len(result)):
                keys = list(aux.keys())
                keys = [str(x) for x in keys]
                object_keys = list(aux.keys())
                if result[i] in keys:
                    indice = keys.index(result[i])
                    if i == len(result) - 1:
                        if object_keys[indice].get_type() == 'd':
                            print('rm: Is a directory')
                        else:
                            del aux[object_keys[indice]]
                    else:
                        aux = aux[object_keys[indice]]

                elif result[i] == '.':
                    pass

                elif result[i] == '..':
                    slashes = [pos for pos, char in enumerate(cur_path) if char == '/']
                    if len(slashes) == 1 :
                        cur_path = '/'
                        pass
                    else:
                        # Imprime el path hasta antes de la ultima slash
                        cur_path = cur_path[:max(slashes)]
                    if cur_path == '/':
                        aux = self.root_bin
                        result_analize = ['/']
                    else:
                        aux = self.root
                        result_analize = self.analize_string(cur_path)

                    if isinstance(result_analize, list):
                        for i in range(len(result_analize)):
                            keys = list(aux.keys())
                            keys = [str(x) for x in keys]
                            object_keys = list(aux.keys())
                            if result_analize[i] in keys:
                                indice = keys.index(result_analize[i])
                                aux = aux[object_keys[indice]]

                else:
                    # En algun punto la ruta no existio
                    print('rm: No such file')
                    break

    def removeDir_command(self, command, cur_dir):
        '''
        Remove a empty directory

        Parameters
        ----------
        command : list
            The command entered by user splitted in a list
            that could be a path or name of file
        cur_dir : dictionary
            start dictionary to search the directory and delete it

        Returns
        -------
        None
        '''

        if len(command) == 1 or len(command) > 2:
            print('rmdir: Invalid syntax')
        elif len(command) == 2:

            if command[1][0] == '/' and len(command[1]) > 1:
                aux = self.root
            else:
                aux = cur_dir            

            if self.cur_path == '/' and command[1] == '..':
                print('rmdir: Cannot remove pwd')
                return

            if self.cur_path == '/' and command[1] == '/':
                print('rmdir: Cannot remove pwd')
                return

            if self.cur_path == command[1]:
                print('rmdir: Cannot remove pwd')
                return

            result = self.analize_string(command[1])
            if len(result) == 0 and self.cur_path != '/':
                print('rmdir: Directory not empty')
            cur_path = self.cur_path
            for i in range(len(result)):
                keys = list(aux.keys())
                keys = [str(x) for x in keys]
                object_keys = list(aux.keys())
                if result[i] in keys:
                    indice = keys.index(result[i])
                    if i == len(result) - 1:
                        if object_keys[indice].get_type() == 'd':
                            if aux[object_keys[indice]]:
                                print('rmdir: Directory not empty')
                                break
                            else:
                                del aux[object_keys[indice]]
                        else:
                            print('rmdir: Not a directory')
                    else:
                        # Avanzamos
                        aux = aux[object_keys[indice]]

                elif result[i] == '.':
                    print('rmdir: Cannot remove pwd')

                elif result[i] == '..':
                    slashes = [pos for pos, char in enumerate(cur_path) if char == '/']
                    if len(slashes) == 1:
                        cur_path = '/'
                        print('rmdir: Directory not empty')
                        pass
                    else:
                        # Imprime el path hasta antes de la ultima slash
                        cur_path = cur_path[:max(slashes)]

                    if cur_path == '/':
                        aux1 = self.root_bin
                        result_analize = ['/']
                    else:
                        aux1 = self.root
                        result_analize = self.analize_string(cur_path)

                    if isinstance(result_analize, list):
                        for i in range(len(result_analize)):
                            keys = list(aux1.keys())
                            keys = [str(x) for x in keys]
                            object_keys = list(aux1.keys())
                            if result_analize[i] in keys:
                                indice = keys.index(result_analize[i])
                                aux1 = aux1[object_keys[indice]]

                else:
                    # En algun punto la ruta no existio
                    print('rmdir: No such file or directory')
                    break

    def adduser_command(self, command, user_list, current_user):
        '''
        Add a new user to the terminal

        Parameters
        ----------
        command : list
            The command entered by user splitted in a list
        user_list : list
            The list with the users
        current_user : user object
            The current user in the terminal
        
        Returns
        -------
        None
        '''

        if current_user.get_name() != 'root':
            print("adduser: Operation not permitted")
            return

        if len(command) == 1:
            print("adduser: Incorrect syntax")
        elif len(command) == 2:
            names = []
            # Comprobar si el usuario existe
            for i in range(len(user_list)):
                names.append(user_list[i].get_name())
            if command[1] in names:
                print('adduser: The user already exists')
            else:
                new_user = User(command[1])
                user_list.append(new_user)

    def delususer_command(self, command, user_list, current_user):
        '''
        Delete existen user in the terminal

        Parameters
        ----------
        command : list
            The command entered by user splitted in a list
        user_list : list
            The list with the users
        current_user : user object
            The current user in the terminal
        
        Returns
        -------
        None
        '''

        if current_user.get_name() != 'root':
            print("deluser: Operation not permitted")
            return

        if len(command) == 1:
            print("adduser: Incorrect syntax")
        elif len(command) == 2:
            names = []
            if command[1] == 'root':
                print('WARNING: You are just about to delete the root account')
                print('Usually this is never required as it may render the whole system unusable')
                print('If you really want this, call deluser with parameter --force')
                print('(but this `deluser` does not allow `--force`, haha)')
                print('Stopping now without having performed any action')
                return
            # Comprobar si el usuario existe
            for i in range(len(user_list)):
                names.append(user_list[i].get_name())
            if command[1] in names:
                indice = names.index(command[1])
                del user_list[indice]
            else:
                print('deluser: The user does not exist')

    def su_command(self, command, user_list, current_user):
        '''
        Change the current user in the terminal if the user exists

        Parameters
        ----------
        command : list
            The command entered by user splitted in a list
        user_list : list
            The list with the users
        current_user : user object
            The current user in the terminal
        
        Returns
        -------
        None        
        '''

        if len(command) == 1:
            self.cur_terminaluser = self.root_user
        elif len(command) == 2:
            names = []
            # Comprobar si el usuario existe
            for i in range(len(user_list)):
                names.append(user_list[i].get_name())
            if command[1] in names:
                indice = names.index(command[1])
                current_user = user_list[indice]
                self.cur_terminaluser = current_user
            else:
                print('su: Invalid user')

    def ls_command(self, command, cur_dir):
        '''
        list the files in directory or the information of
        a file

        Parameters
        ----------
        command : list
            The command entered by user splitted in a list
            to analyze the different parameters
        cur_dir : dictionary
            start dictionary to traversal or list

        Returns
        -------
        None
        '''
        aux = cur_dir

        if len(command) == 1:
            self.ls_name(aux)
            return

        params = command[1:]

        if '-l' in params and '-d' not in params and '-a' not in params:  #ls -l 
            if len(params) == 1:
                self.ls_full(aux)
            else:
                result = params[-1]
                result = self.analize_string(result)
                #print(result)
                for i in range(len(result)):
                    keys = list(aux.keys())
                    keys = [str(x) for x in keys]
                    object_keys = list(aux.keys())

                    if result[i] in keys:
                        indice = keys.index(result[i])
                        if i == len(result) - 1:
                            if object_keys[indice].get_type() == 'd':
                                # The path is a folder
                                # Enter to the folder to list content
                                aux = aux[object_keys[indice]]
                                self.ls_full(aux)
                            else:
                                file = object_keys[indice].get_name()
                                if file[0] == '.':
                                    pass
                                else:
                                    print(object_keys[indice].properties())
                        else:
                            aux = aux[object_keys[indice]]
                    else:
                        print('ls: No such file or directory')

        elif '-l' in params and '-d' in params and '-a' not in params:  # ls -l -d
            if len(params) == 2:
                # Queremos ver solo un puntito
                if self.cur_path == '/':
                    pass
                else:
                    pass
            elif len(params) == 3:
                # Hay un path
                if self.cur_path == '/' and params[2] == '/':
                    keys = list(self.root_bin.keys())
                    keys = [str(x) for x in keys]
                    object_keys = list(self.root_bin.keys())
                    folder_prop = object_keys[0].properties()
                    folder_prop = folder_prop[:-1]
                    folder_prop = folder_prop + '/'
                    print(folder_prop)
                else:
                    result = self.analize_string(params[2])
                    for i in range(len(result)):
                        keys = list(aux.keys())
                        keys = [str(x) for x in keys]
                        object_keys = list(aux.keys())

                        if result[i] in keys:
                            indice = keys.index(result[i])
                            if i == len(result) - 1:
                                if object_keys[indice].get_type() == 'd':
                                    # The path is a folder
                                    file = object_keys[indice].get_name()
                                    if file[0] == '.':
                                        pass
                                    else:
                                        print(object_keys[indice].properties())
                                else:
                                    file = object_keys[indice].get_name()
                                    if file[0] == '.':
                                        pass
                                    else:
                                        print(object_keys[indice].properties())
                            else:
                                aux = aux[object_keys[indice]]
                        else:
                            print('ls: No such file or directory')
                            break

        elif '-l' in params and '-d' not in params and '-a' in params:  #ls -l -a
            if len(params) == 2:
                if self.cur_path == '/':
                    keys = list(self.root_bin.keys())
                    keys = [str(x) for x in keys]
                    object_keys = list(self.root_bin.keys())
                    folder_prop = object_keys[0].properties()
                    folder_prop = folder_prop[:-1]
                    folder_prop = folder_prop + '.'
                    folder_prop2 = folder_prop
                    folder_prop2 = folder_prop2 + '.'
                    print(folder_prop)
                    print(folder_prop2)
                    self.ls_full_dot(aux)
                else:
                    path = self.cur_path
                    result = self.analize_string(path)
                    aux = self.root
                    for i in range(len(result)):
                        keys = list(self.root.keys())
                        keys = [str(x) for x in keys]
                        object_keys = list(self.root.keys())

                        if result[i] in keys:
                            indice = keys.index(result[i])
                            if i == len(result) - 1:
                                if object_keys[indice].get_type() == 'd':
                                    # The path is a folder
                                    folder_prop = object_keys[indice].properties()
                                    spaces = [pos for pos, char in enumerate(folder_prop) if char == ' ']
                                    folder_prop = folder_prop[:spaces[1]] + ' .'
                                    folder_prop2 = folder_prop
                                    folder_prop2 = folder_prop2 + '.'
                                    print(folder_prop)
                                    print(folder_prop2)
                                    aux = aux[object_keys[indice]]
                                    self.ls_full_dot(aux)

                                else:
                                    print(object_keys[indice].properties)
                            else:
                                aux = aux[object_keys[indice]]

            elif len(params) == 3:
                result = self.analize_string(params[2])
                for i in range(len(result)):
                    keys = list(aux.keys())
                    keys = [str(x) for x in keys]
                    object_keys = list(aux.keys())

                    if result[i] in keys:
                        indice = keys.index(result[i])
                        if i == len(result) - 1:
                            if object_keys[indice].get_type() == 'd':
                                # The path is a folder
                                folder_prop = object_keys[indice].properties()
                                spaces = [pos for pos, char in enumerate(folder_prop) if char == ' ']
                                folder_prop = folder_prop[:spaces[1]] + ' .'
                                folder_prop2 = folder_prop
                                folder_prop2 = folder_prop2 + '.'
                                print(folder_prop)
                                print(folder_prop2)
                                aux = aux[object_keys[indice]]
                                self.ls_full_dot(aux)
                            else:
                                print(object_keys[indice].properties())
                        else:
                            aux = aux[object_keys[indice]]
                    else:
                        print('ls: No such file or directory')
                        break

        elif '-l' not in params and '-d' not in params and '-a' not in params:  # ls
            result = params[-1]
            result = self.analize_string(result)

            for i in range(len(result)):
                keys = list(aux.keys())
                keys = [str(x) for x in keys]
                object_keys = list(aux.keys())

                if result[i] in keys:
                    indice = keys.index(result[i])
                    if i == len(result) - 1:
                        if object_keys[indice].get_type() == 'd':
                            # The path is a folder
                            # Enter to the folder to list content
                            aux = aux[object_keys[indice]]
                            self.ls_name(aux)
                        else:
                            file = object_keys[indice].get_name()
                            if file[0] == '.':
                                pass
                            else:
                                print(object_keys[indice].get_name())
                    else:
                        aux = aux[object_keys[indice]]
                else:
                    print('ls: No such file or directory')

        elif '-l' not in params and '-d' not in params and '-a' in params:  # ls -a
            if len(params) == 1:
                if self.cur_path == '/':
                    folder_prop = '.'
                    folder_prop2 = '..'
                    print(folder_prop)
                    print(folder_prop2)
                    self.ls_name_dot(aux)
                else:
                    path = self.cur_path
                    result = self.analize_string(path)
                    aux = self.root
                    for i in range(len(result)):
                        keys = list(self.root.keys())
                        keys = [str(x) for x in keys]
                        object_keys = list(self.root.keys())
                        if result[i] in keys:
                            indice = keys.index(result[i])
                            if i == len(result) - 1:
                                if object_keys[indice].get_type() == 'd':
                                    # The path is a folder
                                    folder_prop = '.'
                                    folder_prop2 = '..'
                                    print(folder_prop)
                                    print(folder_prop2)
                                    aux = aux[object_keys[indice]]
                                    self.ls_name_dot(aux)
                                else:
                                    print(object_keys[indice].get_name())
                            else:
                                aux = aux[object_keys[indice]]

            elif len(params) == 2:
                result = self.analize_string(params[1])

                if params[1] == '.':
                    print('.')
                    print('..')
                    return
                for i in range(len(result)):
                    keys = list(aux.keys())
                    keys = [str(x) for x in keys]
                    object_keys = list(aux.keys())

                    if result[i] in keys:
                        indice = keys.index(result[i])
                        if i == len(result) - 1:
                            if object_keys[indice].get_type() == 'd':
                                # The path is a folder
                                folder_prop = '.'
                                folder_prop2 = '..'
                                print(folder_prop)
                                print(folder_prop2)
                                aux = aux[object_keys[indice]]
                                self.ls_name_dot(aux)
                            else:
                                print(object_keys[indice].get_name())
                        else:
                            aux = aux[object_keys[indice]]
                    else:
                        print('ls: No such file or directory')
                        break

        elif '-l' not in params and '-d' in params and '-a' not in params:  # ls -d
            if len(params) == 1:
                if self.cur_path == '/':
                    pass
                else:
                    pass

            elif len(params) == 2:
                result = self.analize_string(params[1])
                if params[1] == '.':
                    return
                for i in range(len(result)):
                    keys = list(aux.keys())
                    keys = [str(x) for x in keys]
                    object_keys = list(aux.keys())

                    if result[i] in keys:
                        indice = keys.index(result[i])
                        if i == len(result) - 1:
                            if object_keys[indice].get_type() == 'd':
                                # The path is a folder
                                file = object_keys[indice].get_name()
                                if file[0] == '.':
                                    pass
                                else:
                                    print(object_keys[indice].basic_properties())
                            else:
                                file = object_keys[indice].get_name()
                                if file[0] == '.':
                                    pass
                                else:
                                    print(file)
                        else:
                            aux = aux[object_keys[indice]]
                    else:
                        print('ls: No such file or directory')
                        break

        elif '-l' in params and '-d' in params and '-a' in params:  # ls -a -d -l
            if len(params) == 3:
                if self.cur_path == '/':
                    keys = list(self.root_bin.keys())
                    keys = [str(x) for x in keys]
                    object_keys = list(self.root_bin.keys())
                    folder_prop = object_keys[0].properties()
                    folder_prop = folder_prop[:-1]
                    folder_prop = folder_prop + '.'
                    print(folder_prop)
                    #print(folder_prop2)
                    #self.ls_full_dot(aux)
                else:
                    path = self.cur_path
                    result = self.analize_string(path)
                    aux = self.root
                    for i in range(len(result)):
                        keys = list(self.root.keys())
                        keys = [str(x) for x in keys]
                        object_keys = list(self.root.keys())
                        if result[i] in keys:
                            indice = keys.index(result[i])
                            if i == len(result) - 1:
                                if object_keys[indice].get_type() == 'd':
                                    # The path is a folder
                                    folder_prop = object_keys[indice].properties()
                                    spaces = [pos for pos, char in enumerate(folder_prop) if char == ' ']
                                    folder_prop = folder_prop[:spaces[1]] + ' .'
                                    print(folder_prop)
                                    aux = aux[object_keys[indice]]
                            else:
                                aux = aux[object_keys[indice]]

            elif len(params) == 4:
                result = self.analize_string(params[-1])
                for i in range(len(result)):
                    keys = list(aux.keys())
                    keys = [str(x) for x in keys]
                    object_keys = list(aux.keys())

                    if result[i] in keys:
                        indice = keys.index(result[i])
                        if i == len(result) - 1:
                            if object_keys[indice].get_type() == 'd':
                                # The path is a folder
                                print(object_keys[indice].properties())
                            else:
                                print(object_keys[indice].properties())
                        else:
                            aux = aux[object_keys[indice]]
                    else:
                        print('ls: No such file or directory')
                        break

        elif '-l' not in params and '-d' in params and '-a' in params:  # ls -a -d
            if len(params) == 2:
                if self.cur_path == '/':
                    print('.')
                else:
                    print('.')

            elif len(params) == 3:
                result = self.analize_string(params[-1])
                if params[-1] == '.':
                    print('.')
                    return
                for i in range(len(result)):
                    keys = list(aux.keys())
                    keys = [str(x) for x in keys]
                    object_keys = list(aux.keys())

                    if result[i] in keys:
                        indice = keys.index(result[i])
                        if i == len(result) - 1:
                            if object_keys[indice].get_type() == 'd':
                                # The path is a folder
                                file = object_keys[indice].get_name()
                                print(file)
                            else:
                                print(object_keys[indice].get_name())
                        else:
                            aux = aux[object_keys[indice]]
                    else:
                        print('ls: No such file or directory')
                        break

    def chmod_command(self, command, cur_dir):
        '''
        Change the permissions of files

        Parameters
        ----------
        command : list
            The command entered by user splitted in a list
            to analyze the different parameters
        cur_dir : dictionary
            start dictionary to traversal and find the file

        Returns
        -------
        None

        '''
        self.objeto = 0

        if len(command) < 3:
            print('chmod: Invalid syntax')
            return
        if len(command) > 3:
            print('chmod: Invalid syntax')
            return

        if command[2] == '/':
            aux = self.root_bin
            result = ['/']
        else:
            aux = cur_dir
            result = self.analize_string(command[2])  # path to fle

        perms = self.analize_perms(command[1])  # permission list
        a = self.determinant_object(result, aux)
        if a == 2:
            print('chmod: No such file or directory')
            return
        self.change_perms(perms, self.objeto)

    def determinant_object(self, result, aux):
        '''
        Parameters
        ----------
        result : list
            destination path segmented into a list
        aux: dictionary
            start dictionary to search the file

        Returns
        -------
        flag : int
            Based on whether or not the file is found,
            certain useful flags are returned to determine errors.
        '''

        for i in range(len(result)):
            keys = list(aux.keys())
            keys = [str(x) for x in keys]
            object_keys = list(aux.keys())
            if result[i] in keys:
                indice = keys.index(result[i])
                if i == len(result) - 1:
                    if object_keys[indice].get_type() == 'd':
                        flag = 1
                        self.objeto = object_keys[indice]
                        return flag
                    else:
                        flag = 1
                        self.objeto = object_keys[indice]
                        return flag
                else:
                    if object_keys[indice].get_type() == 'd':
                        aux = aux[object_keys[indice]]
                    else:
                        flag = 2  # Mala ruta
                        return flag
            else:
                flag = 2
                return flag

    def change_perms(self, result, file):
        '''
        Change the permissions of the file

        Parameters
        ----------
        result : list
            List that contain the format string splitted
        file : object file/folder
            The object to change the permissions
        
        Returns
        -------
        None
        '''

        if result == [0, 0, 0]:
            print('chmod: Invalid mode')
            return

        if result[0] == 'a':
            if result[1] == '+':
                if result[2] == 'r':
                    file.add_read_ow()
                    file.add_read_ot()
                elif result[2] == 'w':
                    file.add_write_ow()
                    file.add_write_ot()
                elif result[2] == 'x':
                    file.add_exec_ow()
                    file.add_exec_ot()
                elif 'r' in result[2] and 'w' in result[2] and len(result[2]) == 2:
                    file.add_read_ow()
                    file.add_write_ow()
                    file.add_read_ot()
                    file.add_write_ot()
                elif 'r' in result[2] and 'x' in result[2] and len(result[2]) == 2:
                    file.add_read_ow()
                    file.add_exec_ow()
                    file.add_read_ot()
                    file.add_exec_ot()
                elif 'w' in result[2] and 'x' in result[2] and len(result[2]) == 2:
                    file.add_write_ow()
                    file.add_exec_ow()
                    file.add_write_ot()
                    file.add_exec_ot()
                elif 'r' in result[2] and 'w' in result[2] and 'x' in result[2]:
                    file.add_all_ow()
                    file.add_all_ot()
                elif result[2] == '':
                    pass
            elif result[1] == '-':
                if result[2] == 'r':
                    file.del_read_ot()
                    file.del_read_ow()
                elif result[2] == 'w':
                    file.del_write_ot()
                    file.del_write_ow()
                elif result[2] == 'x':
                    file.del_exec_ot()
                    file.del_exec_ow()
                elif 'r' in result[2] and 'w' in result[2] and len(result[2]) == 2:
                    file.del_write_ow()
                    file.del_read_ow()
                    file.del_read_ot()
                    file.del_write_ot()
                elif 'r' in result[2] and 'x' in result[2] and len(result[2]) == 2:
                    file.del_exec_ow()
                    file.del_read_ow()
                    file.del_read_ot()
                    file.del_exec_ot()
                elif 'w' in result[2] and 'x' in result[2] and len(result[2]) == 2:
                    file.del_exec_ow()
                    file.del_write_ow()
                    file.del_write_ot()
                    file.del_exec_ot()
                elif 'r' in result[2] and 'w' in result[2] and 'x' in result[2]:
                    file.del_all_ow()
                    file.del_all_ot()
                elif result[2] == '':
                    pass
            elif result[1] == '=':
                if result[2] == 'r':
                    file.read_only_ow()
                    file.read_only_ot()
                elif result[2] == 'w':
                    file.write_only_ow()
                    file.write_only_ot()
                elif result[2] == 'x':
                    file.exec_only_ow()
                    file.exec_only_ot()
                elif 'r' in result[2] and 'w' in result[2] and len(result[2]) == 2:
                    file.del_all()
                    file.add_read_ow()
                    file.add_read_ot()
                    file.add_write_ow()
                    file.add_write_ot()
                elif 'r' in result[2] and 'x' in result[2] and len(result[2]) == 2:
                    file.del_all()
                    file.add_exec_ow()
                    file.add_read_ow()
                    file.add_read_ot()
                    file.add_exec_ot()
                elif 'w' in result[2] and 'x' in result[2] and len(result[2]) == 2:
                    file.del_all()
                    file.add_exec_ow()
                    file.add_write_ow()
                    file.add_write_ot()
                    file.add_exec_ot()
                elif 'r' in result[2] and 'w' in result[2] and 'x' in result[2]:
                    file.add_all_ow()
                    file.add_all_ot()
                elif result[2] == '':
                    file.del_all()
        elif result[0] == 'u':
            if result[1] == '+':
                if result[2] == 'r':
                    file.add_read_ow()
                elif result[2] == 'w':
                    file.add_write_ow()
                elif result[2] == 'x':
                    file.add_exec_ow()
                elif 'r' in result[2] and 'w' in result[2] and len(result[2]) == 2:
                    file.add_read_ow()
                    file.add_write_ow()
                elif 'r' in result[2] and 'x' in result[2] and len(result[2]) == 2:
                    file.add_read_ow()
                    file.add_exec_ow()
                elif 'w' in result[2] and 'x' in result[2] and len(result[2]) == 2:
                    file.add_write_ow()
                    file.add_exec_ow()
                elif 'r' in result[2] and 'w' in result[2] and 'x' in result[2]:
                    file.add_all_ow()
                elif result[2] == '':
                    pass
            elif result[1] == '-':
                if result[2] == 'r':
                    file.del_read_ow()
                elif result[2] == 'w':
                    file.del_write_ow()
                elif result[2] == 'x':
                    file.del_exec_ow()
                elif 'r' in result[2] and 'w' in result[2] and len(result[2]) == 2:
                    file.del_write_ow()
                    file.del_read_ow()
                elif 'r' in result[2] and 'x' in result[2] and len(result[2]) == 2:
                    file.del_exec_ow()
                    file.del_read_ow()
                elif 'w' in result[2] and 'x' in result[2] and len(result[2]) == 2:
                    file.del_exec_ow()
                    file.del_write_ow()
                elif 'r' in result[2] and 'w' in result[2] and 'x' in result[2]:
                    file.del_all_ow()
                elif result[2] == '':
                    pass
            elif result[1] == '=':
                if result[2] == 'r':
                    file.read_only_ow()
                elif result[2] == 'w':
                    file.write_only_ow()
                elif result[2] == 'x':
                    file.exec_only_ow()
                elif 'r' in result[2] and 'w' in result[2] and len(result[2]) == 2:
                    file.del_all_ow()
                    file.add_read_ow()
                    file.add_write_ow()
                elif 'r' in result[2] and 'x' in result[2] and len(result[2]) == 2:
                    file.del_all_ow()
                    file.add_exec_ow()
                    file.add_read_ow()
                elif 'w' in result[2] and 'x' in result[2] and len(result[2]) == 2:
                    file.del_all_ow()
                    file.add_exec_ow()
                    file.add_write_ow()
                elif 'r' in result[2] and 'w' in result[2] and 'x' in result[2]:
                    file.add_all_ow()
                elif result[2] == '':
                    file.del_all_ow()
        elif result[0] == 'o':
            if result[1] == '+':
                if result[2] == 'r':
                    file.add_read_ot()
                elif result[2] == 'w':
                    file.add_write_ot()
                elif result[2] == 'x':
                    file.add_exec_ot()
                elif 'r' in result[2] and 'w' in result[2] and len(result[2]) == 2:
                    file.add_read_ot()
                    file.add_write_ot()
                elif 'r' in result[2] and 'x' in result[2] and len(result[2]) == 2:
                    file.add_read_ot()
                    file.add_exec_ot()
                elif 'w' in result[2] and 'x' in result[2] and len(result[2]) == 2:
                    file.add_write_ot()
                    file.add_exec_ot()
                elif 'r' in result[2] and 'w' in result[2] and 'x' in result[2]:
                    file.add_all_ot()
                elif result[2] == '':
                    pass
            elif result[1] == '-':
                if result[2] == 'r':
                    file.del_read_ot()
                elif result[2] == 'w':
                    file.del_write_ot()
                elif result[2] == 'x':
                    file.del_exec_ot()
                elif 'r' in result[2] and 'w' in result[2] and len(result[2]) == 2:
                    file.del_write_ot()
                    file.del_read_ot()
                elif 'r' in result[2] and 'x' in result[2] and len(result[2]) == 2:
                    file.del_exec_ot()
                    file.del_read_ot()
                elif 'w' in result[2] and 'x' in result[2] and len(result[2]) == 2:
                    file.del_exec_ot()
                    file.del_write_ot()
                elif 'r' in result[2] and 'w' in result[2] and 'x' in result[2]:
                    file.del_all_ot()
                elif result[2] == '':
                    pass
            elif result[1] == '=':
                if result[2] == 'r':
                    file.read_only_ot()
                elif result[2] == 'w':
                    file.write_only_ot()
                elif result[2] == 'x':
                    file.exec_only_ot()
                elif 'r' in result[2] and 'w' in result[2] and len(result[2]) == 2:
                    file.del_all_ot()
                    file.add_read_ot()
                    file.add_write_ot()
                elif 'r' in result[2] and 'x' in result[2] and len(result[2]) == 2:
                    file.del_all_ot()
                    file.add_exec_ot()
                    file.add_read_ot()
                elif 'w' in result[2] and 'x' in result[2] and len(result[2]) == 2:
                    file.del_all_ot()
                    file.add_exec_ot()
                    file.add_write_ot()
                elif 'r' in result[2] and 'w' in result[2] and 'x' in result[2]:
                    file.add_all_ot()
                elif result[2] == '':
                    file.del_all_ot()

    def chown_command(self, command, cur_dir, user_list, current_user):
        '''
        Change the owner of a file or directory

        Parameters
        ----------
        command : list
            The command entered by user splitted in a list
            to analyze the different parameters
        cur_dir : dictionary
            start dictionary to traversal and find the file
        user_list : list
            The list with all the users
        current_user : user object
            The current user of terminal

        Returns
        -------
        None        
        '''
        self.objeto = 0

        if len(command) < 3 or len(command) > 3:
            print('chown: Invalid syntax')
            return

        if current_user.get_name() != 'root':
            print('chown: Operation not permitted')
            return

        names = []

        for i in range(len(user_list)):
            names.append(user_list[i].get_name())

        if command[1] not in names:
            print('chown: Invalid user')
            return

        aux = cur_dir
        result = self.analize_string(command[2])
        a = self.determinant_object(result, aux)

        if a == 2:
            print('chown: No such file or directory')
            return

        self.objeto.set_user(command[1])

    def analize_perms(self, string):
        '''
        Analize a string to split the different elements to change
        the permissions

        Parameters
        ----------
        string : str
            The string to be analized lookig for permissions, user and 
            =,-,+ symbols

        Returns
        -------
        A list with the parameters splitted
        '''

        if '+' in string:
            action = '+'
            string = string.split('+')
        elif '-' in string:
            action = '-'
            string = string.split('-')
        elif '=' in string:
            action = '='
            string = string.split('=')
        else:
            return [0, 0, 0]

        if string[0] == '':
            return [0, 0, 0]
        allow = set('rwx')
        validation = set((string[1]))
        if validation.issubset(allow):
            pass
        else:
            return [0, 0, 0]

        return [string[0], action, string[1]]

    def ls_full(self, aux):
        '''
        List the files with complete properties inside a path
        without files that start with dot

        Parameters
        ----------
        aux : dictionary
            The dictionary to list
        
        Returns
        -------
        None
        '''

        keys = list(aux.keys())
        keys = [str(x) for x in keys]

        sorted_keys = keys.copy()
        sorted_keys.sort()

        object_keys = list(aux.keys())

        for i in range(len(keys)):
            indice = keys.index(sorted_keys[i])
            file = object_keys[indice].get_name()
            if file[0] == '.':
                pass
            else:
                print(object_keys[indice].properties())

    def ls_name(self, aux):
        '''
        List the files names inside a path without files
        that start with dot

        Parameters
        ----------
        aux : dictionary
            The dictionary to list
        
        Returns
        -------
        None
        '''

        keys = list(aux.keys())
        keys = [str(x) for x in keys]

        sorted_keys = keys.copy()
        sorted_keys.sort()

        object_keys = list(aux.keys())

        for i in range(len(keys)):
            indice = keys.index(sorted_keys[i])
            file = object_keys[indice].get_name()
            if file[0] == '.':
                pass
            else:
                print(object_keys[indice].basic_properties())

    def ls_name_dot(self, aux):
        '''
        List the files names inside a path including files
        that start with dot

        Parameters
        ----------
        aux : dictionary
            The dictionary to list
        
        Returns
        -------
        None
        '''

        keys = list(aux.keys())
        keys = [str(x) for x in keys]

        sorted_keys = keys.copy()
        sorted_keys.sort()

        object_keys = list(aux.keys())

        for i in range(len(keys)):
            indice = keys.index(sorted_keys[i])
            file = object_keys[indice].get_name()
            print(object_keys[indice].basic_properties())

    def ls_full_dot(self, aux):
        '''
        List all the files names inside a path

        Parameters
        ----------
        aux : dictionary
            The dictionary to list
        
        Returns
        -------
        None
        '''
        keys = list(aux.keys())
        keys = [str(x) for x in keys]

        sorted_keys = keys.copy()
        sorted_keys.sort()

        object_keys = list(aux.keys())

        for i in range(len(keys)):
            indice = keys.index(sorted_keys[i])
            print(object_keys[indice].properties())

    def analize_string(self, string):
        '''
        Analize the string to split based on slashes

        Parameters
        ----------

        string : str
            The string that should be a path
        
        Returns
        -------
        A list with the path segmentated
        '''

        if '"' in string:
            if string[0] == '/' and len(string) > 1:
                string = string[1:]
            if string[-1] == '/':
                string = string[:-1]
            if '/' in string:
                string = string.split('/')
                string = [i.replace('"', '') for i in string]
                return string
            else:
                string = string.strip('"')
                string = [string]
                return string
        else:
            if string[0] == '/' and len(string) > 1:
                string = string[1:]
            if string[-1] == '/':
                string = string[:-1]
            if '/' in string:
                string = string.split('/')
                # Array of words that define path
                return string
            else:
                # Name of file to be created
                string = string.split()
                return string

    def analize_symbols(self, string):
        '''
        Parses a string looking for prohibited characters

        Parameters
        ----------

        string : str
            The complete string entered by the user
        
        Returns
        -------
        Boolean value
        '''

        Letters = 'abcdefghijklmnopqrstuvwxyz'
        Capitals = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        Numbers = '0123456789'
        symbols = '_-./" +-='

        Allow = Letters + Capitals + Numbers + symbols
        allowed_chars = set(Allow)

        validation = set((string))

        if validation.issubset(allowed_chars):
            return True
        else:
            return False

    def split_quotes(self, string):
        '''
        Function to split the command without breaking the path
        when there are quotes

        Parameters
        ----------
        string : str
            The command entered by the user

        Returns
        -------
        List with the command splitted 
        '''
        array = []
        word = ''
        string = string.strip()
        flag = False
        for i in range(len(string)):
            if string[i] != ' ':
                word = word + string[i]
                if string[i] == '"':
                    flag = not flag
            elif string[i] == ' ' and flag is True:
                word = word + string[i]
            elif string[i] == ' ' and flag is False:
                array.append(word)
                word = ''
        array.append(word)
        return array


if __name__ == "__main__":
    try:
        Terminal()
    except:
        pass
