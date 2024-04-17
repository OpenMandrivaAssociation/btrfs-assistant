Name:           btrfs-assistant
Version:        2.0
Release:        1
Summary:        GUI management tool to make managing a Btrfs filesystem easier
Group:          System/ 
License:        GPL-3.0-or-later
URL:            https://gitlab.com/btrfs-assistant/btrfs-assistant
Source0:        https://gitlab.com/btrfs-assistant/btrfs-assistant/-/archive/%{version}/btrfs-assistant-%{version}.tar.bz2
Group:          System/Monitoring
Requires:       hicolor-icon-theme
Requires:       polkit
 
BuildRequires:  desktop-file-utils
BuildRequires:  cmake
BuildRequires:  pkgconfig(libbtrfsutil)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  appstream-util
Recommends:     btrfsmaintenance
Recommends:     snapper

%description
Btrfs Assistant is a GUI management tool to make managing a Btrfs filesystem
easier.
 
The primary features it offers are:
 
* An easy to read overview of Btrfs metadata
* A simple view of subvolumes with or without Snapper/Timeshift snapshots
* Run and monitor scrub and balance operations
* A pushbutton method for removing subvolumes
* A management front-end for Snapper with enhanced restore functionality
    * View, create and delete snapshots
    * Restore snapshots in a variety of situations
        * When the filesystem is mounted in a different distro
        * When booted off a snapshot
        * From a live ISO
    * View, create, edit, remove Snapper configurations
    * Browse snapshots and restore individual files
    * Browse diffs of a single file across snapshot versions
    * Manage Snapper systemd units
* A front-end for Btrfs Maintenance
    * Manage systemd units
    * Easily manage configuration for defrag, balance and srub settings
 
%prep
%autosetup -p1
 
# Fix config path for btrfsmaintenance
sed -i 's|^bm_config =.*|bm_config = %{_sysconfdir}/sysconfig/btrfsmaintenance|' src/btrfs-assistant.conf
 
%build
%cmake -DCMAKE_BUILD_TYPE='Release'
%make_build

%install
%make_install -C build
%check
 

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_bindir}/%{name}-bin
%{_bindir}/%{name}-launcher
%{_metainfodir}/%{name}.metainfo.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/polkit-1/actions/org.%{name}.pkexec.policy
%config(noreplace) %{_sysconfdir}/%{name}.conf
