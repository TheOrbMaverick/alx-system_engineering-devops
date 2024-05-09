

Issue summary:
- The outage happened at 6pm WAT and ended about 9pm WAT
- It affected about 10% of users (approximately 1,000 users)
- It was caused by server downtime of one of our host servers



Timeline:
- The issue was detected at about 6:30pm WAT
- The issue was detected when several users in Lagos, Nigeria started to contact support.
- We first checked the code log and no changes had been made recently, then we began to by trying to use VPNs to conect from that location and found that our closest servers in that area was down
- We escalated to Henry in the devops team to contact the server hosts.
- The host confirmed a downtime on their end so we moved our load to outr 2 existing servers till that one was fixed.


Root cause and resolution must contain:
- The issue was caused by an overloadd of the server from other companies sharing the same server with us due to excessive client-side requests. 
The company lacked a proper load balancer. So all of their load was not distributed properly.
- The issue was fixed when the host comapany moved the server-client causing the issue to their own server



Corrective and preventative measures must contain:

- We must stop using hared servers and use only personal servers.
TODO:
- Reasearch afordable web server plans that give us our personal server
- Pay for most affordable server.
- Migrate to those servers

![ry4wE7m](https://github.com/TheOrbMaverick/alx-system_engineering-devops/assets/39674670/170fb401-c4a0-4a00-bd1e-df9a4d37a402)
