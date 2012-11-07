## Contributing

django-twitter-bootstrap is an MIT-licensed, open-source project and welcomes
contributions.

This being a relatively simple project, contributions would likely take one of
the following forms:

 * Any of the items found in the PLAN
 * Backports of this packaging to prior versions of Twitter Bootstrap
 * Minor bugfixes
 * Documentation improvements
 * Tests

I plan to keep up on future releases of Bootstrap myself.

## Developing - The Bootstrap git sub-module

One note of import to would-be contributors is that Bootstrap is included as a
git sub-module so that we don't have the mess of managing *copies* of
Bootstrap's sources. Instead we can just checkout a target release tag of
Bootstrap and go.

When you first clone the project:

```bash
git clone git://github.com/estebistec/django-twitter-bootstrap.git
cd django-twitter-bootstrap
git submodule update --init
```

Then, when you want to update to a different release of Bootstrap:

```bash
cd twitter_bootstrap/static
git checkout v2.2.3 # Or other commit, preferably a release tag
cd ../..
git add twitter_bootstrap/static
git commit -m "Upgrade Twitter Bootstrap to v2.2.3"
```
