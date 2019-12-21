# Bonus assignment - Contribute to a real security project! 
Replace your lowest grade, with whatever you get on this one.


## Part 1 (50 pts):
Perform an in-depth code review and audit of an open source small-medium security related project.
This will be evaluated critically, graded individually, and must include a thorough technical documentation of the code-base, and demonstrate an understanding of the mechanisms of action of the projects whole code-base (or a sub-component, if you chose a bigger project).
You should submit a written report and technical diagrams.
Your report should provide an easy-to-read documentation for the main operation of each project file and component.


The following may help you in writing your code review and audit:
Some of these are more extensive than what you might produce for this assignment, and are just style examples.
I am looking for:
* a full state diagram of the code (images you create), 
* a functional description of the mechanisms in the code, and 
* all in all at least 3-4 pages of analysis. 

### Step 1: 
Read some security audits

Example audit reports for software security:
* https://www.x41-dsec.de/reports/Kudelski-X41-Wire-Report-phase1-20170208.pdf
* https://eprint.iacr.org/2016/1013.pdf
* https://www.nitrokey.com/sites/default/files/NitrokeyFirmwareSecurityAuditReport05-2015.pdf
* https://www.nitrokey.com/sites/default/files/NitrokeyHardwareSecurityAuditReport08-2015.pdf

Example audit reports for pentesting:
* http://www.niiconsulting.com/services/security-assessment/NII_Sample_PT_Report.pdf
* https://github.com/juliocesarfort/public-pentesting-reports
* https://www.sans.org/reading-room/whitepapers/testing/writing-penetration-testing-report-33343
* https://www.offensive-security.com/reports/sample-penetration-testing-report.pdf
* https://darrylmacleod.wordpress.com/2012/03/26/penetration-testing-report-templates/
* http://190.90.112.209/penetration-testing-sample-report.pdf

### Step 2: 
Diagram the code, discuss it's mechanisms, discuss any potential security issues you are considering. 
Deliverable: `pa07-audit.pdf` or `pa07-audit.md` (with images, screenshots, diagrams, etc.)


## Part 2 (50 pts): 
You should try to tackle at least one of the outstanding GitLab or GitHub issues (preferred), and if you can't find any reasonable issues to tackle, find other code-related changes to fix or improve the project (can be simple UI improvements if you can't find any security related issues).
Note: this means you have to actually code the fix, and test your code change to the software, showing a before/after for your change.
Your improvement needs to be implemented and working.
Then when you think the issue is fixed solidly enough, then create a pull/merge request for the main project's leaders to check out your fix.

Deliverable: `pa07-before_after.pdf/md` which details the changes you made, showing screenshots illustrating the impact of your improvement, the GitLab/GitHub discussions, requests, etc.


# Choosing a project
You can choose any popular security related project in popular Linux repos, F-droid, etc., with a GitLab or GitHub under active development.
Note: the project must be security related and in some form of significant public release, like being in the Debian repositories, Pip, F-droid, etc.
You will want to pick a project/component that is small enough (less than 20 files or so) that you can understand it in a week!
You will also want to pick a project written in a language you know!


### General search for a project you might want to review/exlpore

Explore GitLab to see if you find anything you like:
* https://gitlab.com/explore
For example, one on the first page, https://gitlab.com/gnutls/gnutls (maybe a bit big for your choice on this one)


Explore GitHub:
* https://github.com/explore


Explore some common security apps:
* https://prism-break.org/en/all/
* https://www.privacytools.io/ (software options) https://www.privacytools.io/software/


Explore F-droid:
* https://f-droid.org/en/packages/
* If you install on your phone, you can browse all security related projects only (they're guaranteed to be open source).
* Only tackle this if you know how to develop on Android.


Browse the Guardian project's apps:
* https://guardianproject.info/apps/ (the drop down menu to see them)
* Many viewable in F-droid.



### Example projects


PixelKnot:
* https://guardianproject.info/apps/info.guardianproject.pixelknot/


OpenSnitch:
* https://www.opensnitch.io/
* https://github.com/evilsocket/opensnitch/
* https://securityonline.info/opensnitch/
* https://en.wikipedia.org/wiki/Personal_firewall


GUFW
* http://gufw.org/
* https://code.launchpad.net/gui-ufw


KeepPassXC
* https://en.wikipedia.org/wiki/KeePassXC
* https://github.com/keepassxreboot/keepassxc


Wire (larger, could choose some sub-component)
* https://wire.com/en/
* https://github.com/wireapp


Gajim OMEMO
* reasonably small python project sub-module
* https://dev.gajim.org/gajim/gajim-plugins
* https://dev.gajim.org/gajim/gajim-plugins/issues
* https://dev.gajim.org/gajim/gajim-plugins/wikis/OmemoGajimPlugin
* https://github.com/omemo/gajim-omemo


Conversations OMEMO
* https://github.com/siacs/Conversations


Enigmail
* https://gitlab.com/enigmail/enigmail


Mailvelop
* https://www.mailvelope.com/ 

