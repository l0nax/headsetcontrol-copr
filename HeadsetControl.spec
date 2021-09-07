Name:           {{{ git_dir_name }}}
Version:        {{{ git_dir_version }}}
Release:        1%{?dist}
Summary:        Sidetone and Battery status for Logitech G930, G533, G633, G933 SteelSeries Arctis 7/PRO 2019 and Corsair VOID (Pro) in Linux and MacOSX

License:        GPL-3.0
URL:            https://github.com/Sapd/HeadsetControl
Source0:        https://github.com/Sapd/HeadsetControl

BuildRequires:  cmake,g++,hidapi-devel,git

%description
Sidetone and Battery status for Logitech G930, G533, G633, G933 SteelSeries Arctis 7/PRO 2019 and Corsair VOID (Pro) in Linux and MacOSX

%prep
git clone https://github.com/Sapd/HeadsetControl
cd HeadSetControl
mkdir build
cd build
cmake ..

%build
%make_build


%install
%make_install


%check


%files
%license
%doc


%changelog

