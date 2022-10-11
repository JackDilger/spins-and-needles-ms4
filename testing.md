### Validator Testing 

***

## CSS Validation

- [W3C CSS Validation](https://validator.w3.org/)- All CSS files were manually inputted in to the validator, no errors are returned. As well as base.css in the spins_and_needles app, CSS files can be found in both the checkout and profile app.

## HTML Validation

- [WC3 Mark Up Validation](https://validator.w3.org/)- All HTML files were manually inputted in to the validator, no errors are returned in all files other than the ones stated below.

- In base.html the JavaScript for the toasts function has been left in this file due to the reasons stated above.
- In checkout.html there is an unresolved 'empty heading' warning from line 132, column 5; to line 132, column 43. This is being used to display the loading spinner when processing payment, I could not find a resolution that would not break this functionality so this has been left again for the reasons stated above.


## JavaScript Validation

- [Js Hint](https://jshint.com/)- All JavaScript files were manually inputted in to the validator, no errors are returned in all files other than the ones stated below.

As mentioned already above and in the bugs section, there were some complications with JavaScript validation. In all 3 instances mentioned below I could not get the files to validate without out breaking the intended functionality. When removing the script tags seen in each JavaScript file mentioned below, the function breaks. However, JS Hint will not validate the files without removing the script tags. I could not find a resolution that would not break this functionality so this has been left again for the reasons stated above.

Impacted files:
- Bag App- update_remove_script.js
- Products App- image_field_edit_script.js
- Products App- image_field_add_script.js


## Python Validation

I used the pep8 validator in GitPod to validate all of my python code, no errors are now shown in the problems tab. Instructions
below on how I used this tool:

- Run the command pip3 install pycodestyle, note that this extension may already be installed, in which case this command will do nothing.
- In your workspace, press Ctrl+Shift+P (or Cmd+Shift+P on Mac).
- Type the word linter into the search bar that appears and click on Python
- Select pycodestyle from the list.
- PEP8 errors will now be underlined in red, as well as being listed in the PROBLEMS tab beside your terminal.

 
