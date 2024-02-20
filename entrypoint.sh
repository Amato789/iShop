#!/bin/bash

# Function for waiting for port availability
wait_for_port() {
    local host=${POSTGRES_HOST}
    local port=${POSTGRES_PORT}
    local timeout=10
    local start_time=$(date +%s)

    # Trying to use ncat, if it installed
    local nc_command="nc"
    type $nc_command >/dev/null 2>&1 || nc_command="ncat"

    while ! $nc_command -z "$host" "$port" >/dev/null 2>&1; do
        sleep 1
        local current_time=$(date +%s)
        local elapsed_time=$((current_time - start_time))
        echo "trying to connecto to pg via $host:$port"

        if [ $elapsed_time -ge $timeout ]; then
            echo "Unable to connect to pg"
            exit 1
        fi
    done
}

# Waiting for available PostgreSQL port
wait_for_port

# Run Django-application
python manage.py runserver 0.0.0.0:8000


#!/bin/sh
if ! [ -f ~/.gnupg/trustdb.gpg ] ; then
  chmod 700 ~/.gnupg/
  gpg --quick-generate-key stripe-live # This will generate a gpg key called "stripe-live"
fi
if ! [ -f ~/.password-store/.gpg-id ] ; then
  pass init stripe-live # This will initialize a password store record named "stripe-live", using the gpg key above
  pass insert stripe-live # This will insert value for the password store "stripe-live", which we will put Stripe Live Secret Key in
fi

string="$@"
liveflag="--live"

if [ -z "${string##*$liveflag*}" ] ;then
  OPTS="--api-key $(pass show stripe-live)" # This will use the content of the password store "stripe-live" which was inserted in line 8
fi

#pass insert stripe-live
/bin/stripe  $@ $OPTS