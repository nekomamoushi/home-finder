# Home Finder

This bot will scrape different apartment provider and find results matching your criteria.
It has to be run periodically and if he finds new results, you will be notify.

## Settings

First, you need to fill the settings with your criterias.
You can use this [sample](samples/settings.yml).

### Search

* `price`:
  * `MIN`
  * `MAX`

* `surface`:
  * `MIN`
  * `MAX`
* `rooms`
* `bedrooms`
* `cities`


### Notification

* `name`: the notifier name
* `type`: the type of notification
* `trigger`: the trigger

## Limitation

For now, there is only:

* One provider: [SELOGER](www.seloger.com)
* One notifier: [IFTTT](www.ifttt.com)
  * one type: `webhook`


## Setup

Before using this bot, you'll need an account on IFTTT:

* Create an acccount if you don't have on
* Create a webhook service
* fill the settings with trigger
* export the variable `NOTIFY_TOKEN` with the IFTTT key

## Usage

The entry point:

```
python src/roof_boot/cli.py
```

The first time you will run the bot, it will create a database of all the results.
It will return the search url used for getting all the result (you can see the results on your favorite browser).

Then the second time you run it, it will notify you by mail if there are new results compare to the first search.

