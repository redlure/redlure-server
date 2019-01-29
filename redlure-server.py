from app import app, db
from app.models import User, Profile, Role, Workspace, List, Person, Email, Page, Domain, Campaign, Result, Server, APIKey

# objects to initialize 'flask shell' with
@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'User': User,
        'Profile': Profile,
        'Role': Role,
        'Workspace': Workspace,
        'List': List,
        'Person': Person,
        'Email': Email,
        'Page': Page,
        'Domain': Domain,
        'Campaign': Campaign,
        'Result': Result,
        'Server': Server,
        'APIKey': APIKey
    }