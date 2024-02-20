# Write your code here
def format_time(hours, minutes, seconds):
    def format(input):
        return str(input).rjust(2,"0")
    return f'{format(hours)}:{format(minutes)}:{format(seconds)}'