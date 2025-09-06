# create-form-method3
This method shows how to create a secure Django form by defining it in forms.py, handling input in views.py, linking it to a database model in models.py, and displaying it in form.html. Data protection is ensured using validation, CSRF tokens, and automatic escaping in Django templates.
Django Form Creation with Data Protection

This guide explains how to create and use a form in Django with proper data handling and protection.

Steps

1. Create the Form

Define the form inside pages/forms.py.

Use a Meta class to link it with a model and specify allowed fields.

Apply Django’s built-in field validation to ensure correct input.



2. Receive Form Data

In pages/views.py, handle the submitted form.

Use form.is_valid() to check if the data is correct.

Cleaned and validated data is accessed through form.cleaned_data.



3. Create Database Table

Define the model in pages/models.py.

Run migrations to create a secure table in the database.



4. Create the Template

Design the form in templates/pages/form.html.

Use Django template tags ({{ form.as_p }}) to avoid manual HTML injection.




Data Protection

Validation: Only save data after form.is_valid().

CSRF Protection: Use {% csrf_token %} in your template to prevent cross-site attacks.

Field Restrictions: Allow only specific fields in Meta to avoid unwanted data entry.

Escaping: Django templates automatically escape user input to protect against XSS.


Summary

By following these steps, you can safely create a Django form, connect it to the database, handle user input securely, and display it on a webpage.
