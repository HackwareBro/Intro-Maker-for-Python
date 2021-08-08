# Python Intro Maker
 Make some interesting intros in the start of loading any of your terminal based python program.

I will update this program time to time!

## Installation

Install required modules for this python program by typing:
`pip3 install -r requirements.txt`

## Usage
![intro](https://user-images.githubusercontent.com/85396426/128628092-b3fd30b9-86be-4649-b644-63533c31a5d3.gif)

Just import this module in any of your program

`import Intro`

and also import

`from colorama import Fore, Back`

to use different colors in your program

<hr>

and you can use anytype of intro design by calling its method, just like the below 

`Intro.blinking('Hackware Bro',cycle=5, color_shade=[Fore.RED,Fore.WHITE,Fore.MAGENTA], 'doom')`

If you forget the names of the colors then just simply type `print(Intro.COLORS)` to print the list of color names and then you can use these colors just like `Fore.RED` or `Back.BLUE`. 
'*Fore*' for text color and '*Back*' for background color

If you forget the names of the fonts then just simply type `print(Intro.FONTS)` to print the list of font names and then you can use these fonts as an argument for the `blinking(font='<fontname>')`

You can also check the fonts' visualization by directly going to figlet website: http://www.figlet.org/examples.html



## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D


<hr>
<div align = "center">
<h3><b>Connect with me:</b></h3>
</div>

<div align="center">
<a href="https://www.youtube.com/channel/UCjLXbCSK44Fw5c_6J8mmZtQ?sub_confirmation=1"><img src="https://img.shields.io/youtube/channel/subscribers/UCjLXbCSK44Fw5c_6J8mmZtQ?label=Hackware%20Bro&style=social" /></a>
<a href="https://twitter.com/HackwareBro"><img src="https://img.shields.io/twitter/follow/HackwareBro?style=social" /></a>
</div>
