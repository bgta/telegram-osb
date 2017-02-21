#
# spec file for package telegram
#
# Copyright (c) 2016 Marcelo Atie, Rio de Janeiro, Brazil.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

Name:		telegram
Version:	1.0.14
Release:	1%{?dist}
Summary:	Official Telegram Messenger app
License:	GPL-3.0
Group:		Productivity/Networking/Instant Messenger
Url:		https://telegram.org/
BuildRequires: xz
BuildRequires:  hicolor-icon-theme
%ifarch x86_64
Source0:	    tsetup.%{version}.tar.xz
%else
Source0:	    tsetup32.%{version}.tar.xz
%endif
Source1:    %{name}.desktop
Source2:    %{name}.png
BuildRoot:	%{_tmppath}/%{name}-%{version}-build

%description
Telegram is a cloud-based mobile and desktop messaging app with a focus on security and speed.

%prep
%setup -q -c

%install

install -Dm 755 Telegram/Telegram %{buildroot}%{_bindir}/%{name}
install -Dm 644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop
install -Dm 644 %{SOURCE2} %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
export NO_BRP_CHECK_RPATH=true

%clean

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%defattr(644,root,root)
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
* Tue Feb 21 2017 Raúl Romero García <bgta@opensuse.org> - 1.0.14-1
- Telegram Desktop was updated to version 1.0.14.
* Mon Feb 6 2017 Raúl Romero García <bgta@opensuse.org> - 1.0.5-1
- Telegram Desktop was updated to version 1.0.5.
* Tue Jan 24 2017 Raúl Romero García <bgta@opensuse.org> - 1.0.2-1
- Telegram Desktop was updated to version 1.0.2.
* Thu Jan 12 2017 Raúl Romero García <bgta@opensuse.org> - 1.0.0-1
- Telegram Desktop was updated to version 1.0.0.
* Thu Dec 22 2016 Raúl Romero García <bgta@opensuse.org> - 0.10.20-1
- Telegram Desktop was updated to version 0.10.20.
* Tue Oct 25 2016 Raúl Romero García <bgta@opensuse.org> - 0.10.19-1
- Telegram Desktop was updated to version 0.10.19.
* Thu Oct 20 2016 Raúl Romero García <bgta@opensuse.org> - 0.10.16-1
- Telegram Desktop was updated to version 0.10.16.

* Wed Oct 05 2016 Raúl Romero García <bgta@opensuse.org> - 0.10.11-1
- Telegram Desktop was updated to version 0.10.11: Bug fixes and other minor improvements

* Wed Oct 05 2016 Raúl Romero García <bgta@opensuse.org> - 0.10.10-1
- Update to version 0.10.10-1
* Mon Oct 03 2016 Raúl Romero García <bgta@opensuse.org> - 0.10.9-1
- Update to version 0.10.9-1
* Sun Sep 25 2016 Raúl Romero García <bgta@opensuse.org> - 0.10.8-1
- Initial package
