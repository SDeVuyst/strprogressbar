
class ProgressBar:

    def __init__(self, value:int, total:int, string_length:int, unfilled_char:str = "▬", progress_char:str = "🔘", fill_bar:bool = False):
        """Create a progress bar

        Args:
            value (int): Current value of the progress bar
            total (int): Max value of the progress bar
            string_length (int): Length of the bar
            unfilled_char (str, optional): char that displays the unfilled portion of the bar. Defaults to "▬".
            progress_char (str, optional): char that displays the filled portion of the bar. Defaults to "🔘".
            fill_bar (bool, optional): If the left side of the bar should also be filled. Defaults to False.

        Raises:
            ValueError: 'value' must be int
            ValueError: 'total' must be int
            ValueError: 'string_length' must be int
            ValueError: 'unfilled_char' must be str
            ValueError: 'progress_char' must be str
            ValueError: 'fill_bar' must be bool
            ValueError: 'value' must be >= 0
            ValueError: 'total' must be >= 0
            ValueError: 'string_length' must be >= 3
        """

        # check for correct args types
        if not isinstance(value, int): raise ValueError(f"'value' must be int, but was {type(value).__name__}")
        if not isinstance(total, int): raise ValueError(f"'total' must be int, but was {type(total).__name__}")
        if not isinstance(string_length, int): raise ValueError(f"'string_length' must be int, but was {type(string_length).__name__}")
        if not isinstance(unfilled_char, str): raise ValueError(f"'unfilled_char' must be str, but was {type(unfilled_char).__name__}")
        if not isinstance(progress_char, str): raise ValueError(f"'progress_char' must be str, but was {type(progress_char).__name__}")
        if not isinstance(fill_bar, bool): raise ValueError(f"'fill_bar' must be bool, but was {type(fill_bar).__name__}")

        # check for args values
        if not 0 <= value: raise ValueError(f"'value' must be >= 0, but was {value}")
        if not 0 <= total: raise ValueError(f"'total' must be >= 0, but was {total}")
        if not 3 <= string_length: raise ValueError(f"'string_length' must be >= 3, but was {string_length}")


        self.string_length = string_length
        self.value = value
        self.total = total
        self.unfilled_char = unfilled_char
        self.progress_char = progress_char
        self.fill_bar = fill_bar

        self.percentage = {
            "enabled": False,
            "left": False,
            "decimals": 0,
            "seperator": " "
        }
        self.counter = {
            "enabled": False,
            "left": False,
            "seperator": " "
        }
    

    def __str__(self) -> str:
        """Returns a string representation of the progress bar

        Returns:
            str: the progressbar
        """

        left, right, perc = self.__generate_bar_figures()

        # generate the base progress unfilled_char
        if self.fill_bar:
            unfilled_char = self.progress_char * (left+1) + self.unfilled_char*right    
        else:
            unfilled_char = self.unfilled_char*left + self.progress_char + self.unfilled_char*right

        # add percentage if necessary
        if self.percentage["enabled"]:
            if self.percentage["left"]:
                unfilled_char = f"%.{self.percentage['decimals']}f%%{self.percentage['seperator']}" % perc + unfilled_char
            else:
                unfilled_char = unfilled_char + f"{self.percentage['seperator']}%.{self.percentage['decimals']}f%%" % perc
        
        # add counter if necessary
        if self.counter["enabled"]:
            if self.counter["left"]:
                unfilled_char = f"{self.value}/{self.total}{self.counter['seperator']}" + unfilled_char  
            else:
                unfilled_char = unfilled_char + f"{self.counter['seperator']}{self.value}/{self.total}"
        
        return unfilled_char
    

    def add_percentage(self, decimals:int = 0, left:bool = False, seperator:str = " "):
        """Adds a percentage number to the progress bar

        Args:
            decimals (int, optional): The amount of decimals to display. Defaults to 0.
            left (bool, optional): If the percentage should be displayed to the left of the progress bar. Defaults to False/right side.
            seperator (str, optional): The seperator between the progress bar and the percentage number. Defaults to " ".

        Raises:
            ValueError: 'decimals' must be int
            ValueError: 'left' must be bool
            ValueError: 'seperator' must be bool
            ValueError: 'decimals' must be between 0 & 5

        Returns:
            ProgressBar: the adapted progressbar
        """

        # check for correct args types
        if not isinstance(decimals, int): raise ValueError(f"'decimals' must be int, but was {type(decimals).__name__}")
        if not isinstance(left, bool): raise ValueError(f"'left' must be bool, but was {type(left).__name__}")
        if not isinstance(seperator, str): raise ValueError(f"'seperator' must be str, but was {type(seperator).__name__}")

        # check for args values
        if not 0 <= decimals <= 5: raise ValueError(f"decimals must be between 0 & 5, but was {decimals}")
                
        self.percentage = {
            "enabled": True,
            "left": left,
            "decimals": decimals,
            "seperator": seperator
        }
        return self
    

    def remove_percentage(self):
        """Remove the percentage

        Raises:
            Exception: percentage is not enabled

        Returns:
            ProgressBar: the adapted progressbar
        """
        if not self.percentage["enabled"]: raise Exception("percentage is not enabled")
        self.percentage["enabled"] = False
        return self


    def add_counter(self, left:bool = False, seperator:str = " "):
        """Adds a counter to the progressbar

        Args:
            left (bool, optional): If the percentage should be displayed to the left of the progress bar. Defaults to False/right side.
            seperator (str, optional): The seperator between the progress bar and the percentage number. Defaults to " ".

        Raises:
            ValueError: 'left' must be bool
            ValueError: 'seperator' must be bool

        Returns:
            ProgressBar: the adapted progressbar
        """
        if not isinstance(left, bool): raise ValueError(f"'left' must be bool, but was {type(left).__name__}")
        if not isinstance(seperator, str): raise ValueError(f"'seperator' must be str, but was {type(seperator).__name__}")

        self.counter = {
            "enabled": True,
            "left": left,
            "seperator": seperator
        }
        return self


    def remove_counter(self):
        """Remove the counter

        Raises:
            Exception: Counter is not enabled

        Returns:
            ProgressBar: the adapted progressbar
        """
        if not self.counter["enabled"]: raise Exception("counter is not enabled")
        self.counter["enabled"] = False
        return self
    

    def __generate_bar_figures(self):
        """Calculate the figures for the bar

        Returns:
            tuple: characters to the left of progress_char, characters to the right, percentage
        """
        perc = self.value/self.total
        left_side = round(perc*self.string_length)
        right_side = self.string_length - left_side

        return left_side-1, right_side, perc*100