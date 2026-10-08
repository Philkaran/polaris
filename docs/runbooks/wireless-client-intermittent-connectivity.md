# Intermittent connectivity on wireless client devices

**Type:** field runbook, from ISP and network operations experience
**Applies to:** a wireless client radio (subscriber module) connected to an access point sector, behind a router

## Purpose

Find and fix the cause of a customer connection that drops or slows at random, in a fixed order, so that a technician, a call-centre agent or a support engineer reaches the same answer.

## When to use it

- The customer reports random drops, or slow speeds at certain times
- Monitoring shows the client radio disconnecting and reconnecting
- The sector itself is healthy and other customers on it are fine

## Likely causes, in the order to check

1. The wireless signal is too weak for the service the customer pays for
2. The Ethernet link between the radio and the router negotiated a poor speed or duplex
3. The radio runs an older firmware version than the access point

## Prerequisites

- Read access to the access point or monitoring system, to see signal data per client
- Administrative access to the router and to the client radio
- Your organisation's minimum signal values per service tier
- A change window if a firmware upgrade is needed

## Steps

### 1. Confirm the scope

Check whether one customer or several are affected. If several clients on the same sector drop together, stop here and investigate the sector, the backhaul or interference instead.

### 2. Check the wireless signal

Open the client list on the access point or the monitoring system and look at the signal level, signal-to-noise ratio, modulation rate and link quality for this client. Compare the signal with the minimum your organisation sets for the customer's service tier.

- Signal below the minimum: realign the antenna, check line of sight, and re-test. If it cannot be fixed, the customer needs a different position or a different service tier.
- Signal fine: continue.

### 3. Check the router port

On the router, open the interface the client radio is plugged into and read the link status: rate and duplex.

- A healthy link negotiates at the full rate and full duplex that the hardware supports.
- A link at 10 Mbps, or at half duplex, points to a cable, port or power injector problem.

### 4. Check the radio's own Ethernet status

Even when the router shows a healthy link, confirm from the radio's side. To reach the radio's management page, use the management network where one exists. If you must use a temporary port forward, restrict it to your own source address, and remove it as soon as you are done (see the security notes).

- Expected: full rate and full duplex on the radio's Ethernet status.
- If not: replace the cable, move to another router port, or replace the injector, then check again until the link is healthy.

### 5. Check the firmware

Compare the radio's firmware version with the access point's version.

- Lower on the radio: upgrade it to match the access point, in a change window.
- During an upgrade, never interrupt power, because that can corrupt the device.
- Keep the previous firmware file available in case you need to roll back.

### 6. Re-test and record

Run a continuous ping and a speed test that stays constant for at least two minutes. Record the signal values, link rate, duplex, firmware versions and what you changed.

## How to verify the fix

- A continuous ping runs without loss for the agreed period
- Throughput stays stable and matches the service tier
- The client radio's session uptime keeps growing, with no reconnects over the next 24 hours

## How to undo

- Remove any temporary port forward or firewall rule you added
- Restore the previous firmware or the saved configuration if the change made things worse
- Put cables and ports back as they were if the change did not help, and note it

## Security notes

- Never leave a management page reachable from the internet. A temporary port forward must be limited to one source address and removed after the check
- Use unique credentials per device, or central authentication, and never write credentials into runbooks, screenshots or tickets
- Redact customer names and addresses from anything you share

## Origin

Written from my own field experience in ISP operations, generalised so that it contains no employer or customer information.
