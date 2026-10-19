Summary:		GUI management tool to make managing a Btrfs filesystem easier
Name:	btrfs-assistant
Version:		3.0.0
Release:		1
License:		GPLv3+
Group:	System/Monitoring
Url:		https://gitlab.com/btrfs-assistant/btrfs-assistant
Source0:	https://gitlab.com/btrfs-assistant/btrfs-assistant/-/archive/%{version}/btrfs-assistant-%{version}.tar.bz2
BuildRequires:		appstream-util
BuildRequires:		cmake >= 3.16
BuildRequires:		desktop-file-utils
BuildRequires:		make
BuildRequires:		cmake(Qt6DBus)
BuildRequires:		cmake(Qt6LinguistTools)
BuildRequires:		cmake(Qt6Widgets)
BuildRequires:		pkgconfig(gl)
BuildRequires:		pkgconfig(libbtrfsutil)
BuildRequires:		pkgconfig(vulkan)
Requires:	btrfs-progs
Requires:	hicolor-icon-theme
Requires:	polkit
Recommends:	btrfsmaintenance
Recommends:	snapper

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

%files
%license LICENSE
%doc changelog README.md
%{_bindir}/%{name}
%{_libexecdir}/%{name}
%{_unitdir}/%{name}-helper.service
%{_datadir}/dbus-1/system-services/org.btrfsassistant.Helper1.service
%{_datadir}/dbus-1/system.d/org.btrfsassistant.Helper1.conf
%{_datadir}/polkit-1/actions/org.btrfsassistant.policy
%{_metainfodir}/%{name}.metainfo.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}.conf

#-----------------------------------------------------------------------------

%prep
%autosetup -p1

# Fix config path for btrfsmaintenance
sed -i 's|^bm_config =.*|bm_config = %{_sysconfdir}/sysconfig/btrfsmaintenance|' src/btrfs-assistant.conf


%build
%cmake -DCMAKE_BUILD_TYPE=Release \
	-DBTRFS_ASSISTANT_HELPER_LIBEXEC=ON \
	-DBTRFS_ASSISTANT_SYSTEMD_UNIT_DIR=%{_unitdir}
%make_build


%install
%make_install -C build
