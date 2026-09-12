*This activity has been created as part of the 42 curriculum by eabushak*

# born2beroot

## Description
Born2beRoot is a System Administration project that introduces the fundamentals of virtualization and server configuration. The goal is to set up a strictly controlled virtual environment using VirtualBox, implementing security policies, user management, and automated monitoring without the use of a graphical interface.

## Instructions

### 1. Installation
* **Virtualization Software:** Install VirtualBox (or UTM).
* **Operating System:** Download the latest stable Debian ISO.
* **Disk Partitioning:** Set up LVM with at least two encrypted partitions.

### 2. Execution
* Start the VM in VirtualBox.
* Log in via the terminal or connect remotely using SSH on port 4242:
  `ssh <your_login>@<ip_address> -p 4242`
* The `monitoring.sh` script will automatically broadcast system status to all terminals every 10 minutes via `wall`.

## Resources
* [Debian Official Documentation](https://www.debian.org/doc/)
* [Sudoers Manual](https://man7.org/linux/man-pages/man5/sudoers.5.html)
* [LVM Guide for Beginners](https://wiki.debian.org/LVM)

### AI Usage Disclosure
* **Tasks:** Used to refine the comparative differences between Linux security modules and firewalls to ensure technical accuracy.
* **Parts:** The Technical Comparisons subsection of the Project description.

## Project description

### OS Choice: Debian
For this project, **Debian** was selected over Rocky Linux.
* **Advantages:** It is highly stable, has a simpler package management system (`apt`), and is widely documented for beginners.
* **Disadvantages:** Its focus on stability means it often lacks the absolute latest versions of software compared to Rocky/RHEL-based systems.

### Main Design Choices
* **Partitioning:** Configured with LVM (Logical Volume Manager) to allow for easy resizing. The volumes are encrypted using LUKS to ensure data at rest is secure.
* **Security Policies:** Implemented a strong password policy (minimum 10 characters, including uppercase and digits) and limited `sudo` attempts.
* **User Management:** Created specific user groups and restricted access to the `sudo` group to maintain the principle of least privilege.
* **Services Installed:** Configured `OpenSSH` for remote management and `UFW` to control incoming and outgoing traffic.

### Comparisons

#### Debian vs Rocky Linux
Debian is a community-driven Linux distribution known for its stability and user-friendly `.deb`/`apt` ecosystem. Rocky Linux is a downstream, corporate-focused build designed to be 100% bug-for-bug compatible with Red Hat Enterprise Linux (RHEL). Rocky uses the `.rpm`/`dnf` ecosystem and is generally more complex for beginners.

#### AppArmor vs SELinux
Both are Mandatory Access Control (MAC) systems. AppArmor (used in Debian) is path-based, restricting programs based on their file system paths, making it relatively straightforward to configure. SELinux (used in Rocky) is label-based, assigning strict security contexts to files, processes, and ports. SELinux offers deeper granularity but has a much steeper learning curve.

#### UFW vs firewalld
UFW (Uncomplicated Firewall) is the default, simplified firewall configuration tool for Debian/Ubuntu, designed to make standard `iptables` management easier. `firewalld` is the default for Rocky Linux and dynamically manages network traffic using a "zone" system to define the trust level of different network connections.

#### VirtualBox vs UTM
VirtualBox is a widely used, type-2 hypervisor for x86/amd64 architectures. UTM is a virtualization and emulation app specifically built for macOS and iOS. It uses QEMU under the hood, making it essential for users on Apple Silicon (M1/M2/M3) Macs who need to emulate x86 environments, as VirtualBox does not natively support those chips.
