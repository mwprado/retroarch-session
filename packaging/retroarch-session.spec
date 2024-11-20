Name:           retroarch-session
Version:        1.0.1alpha
Release:        1%{?dist}
Summary:        Wayland and X11 session desktop file for RetroArch

License:        GPLv3
URL:            https://github.com/mwprado/retroarch-session
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildArch:      noarch

Requires:       retroarch

%description
This package provides session desktop files for RetroArch, allowing it to be launched as a standalone session in both Wayland and X11 environments.

%prep
# Extract the source code
%setup -q -n retroarch-session-main

%build
# No build steps needed for this package

%install
# Create necessary directories
mkdir -p %{buildroot}/usr/share/wayland-sessions
mkdir -p %{buildroot}/usr/share/xsessions

# Install the .desktop file to both locations
install -m 0644 retroarch.desktop %{buildroot}/usr/share/wayland-sessions/retroarch.desktop
install -m 0644 retroarch.desktop %{buildroot}/usr/share/xsessions/retroarch.desktop

%files
%license LICENSE
/usr/share/wayland-sessions/retroarch.desktop
/usr/share/xsessions/retroarch.desktop

%changelog
* Wed Nov 20 2024 Your Name <youremail@example.com> - 1.0-1
- Initial package creation with support for Wayland and X11 sessions under GPLv3
