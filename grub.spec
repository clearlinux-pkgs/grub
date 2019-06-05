#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : grub
Version  : 2.02.beta2
Release  : 19
URL      : http://localhost/cgit/projects/grub/snapshot/grub-2.02-beta2.tar.gz
Source0  : http://localhost/cgit/projects/grub/snapshot/grub-2.02-beta2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC-BY-SA-3.0 GPL-3.0 ICU
Requires: grub-bin
Requires: grub-data
Requires: grub-doc
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : bison
BuildRequires : flex
BuildRequires : freetype-dev
BuildRequires : gettext-bin
BuildRequires : help2man
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : parted-dev
BuildRequires : pkg-config-dev

BuildRequires : texinfo
BuildRequires : xz-dev
Patch1: 0001-Lower-test-timeout.patch
Patch2: 0003-Add-support-for-linuxefi.patch
Patch3: 0004-Use-linuxefi-and-initrdefi-where-appropriate.patch

%description
This is GRUB 2, the second version of the GRand Unified Bootloader.
GRUB 2 is rewritten from scratch to make GNU GRUB cleaner, safer, more
robust, more powerful, and more portable.

%package bin
Summary: bin components for the grub package.
Group: Binaries
Requires: grub-data

%description bin
bin components for the grub package.


%package data
Summary: data components for the grub package.
Group: Data

%description data
data components for the grub package.


%package doc
Summary: doc components for the grub package.
Group: Documentation

%description doc
doc components for the grub package.


%package extras
Summary: extras components for the grub package.
Group: Default

%description extras
extras components for the grub package.


%prep
%setup -q -n grub-2.02-beta2
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1510692989
export CFLAGS="-O3 -g -fopt-info-vec "
unset LDFLAGS
%autogen --disable-static --disable-werror \
--with-platform=efi
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1510692989
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
/usr/lib64/grub/x86_64-efi/acpi.mod
/usr/lib64/grub/x86_64-efi/acpi.module
/usr/lib64/grub/x86_64-efi/adler32.mod
/usr/lib64/grub/x86_64-efi/adler32.module
/usr/lib64/grub/x86_64-efi/affs.mod
/usr/lib64/grub/x86_64-efi/affs.module
/usr/lib64/grub/x86_64-efi/afs.mod
/usr/lib64/grub/x86_64-efi/afs.module
/usr/lib64/grub/x86_64-efi/ahci.mod
/usr/lib64/grub/x86_64-efi/ahci.module
/usr/lib64/grub/x86_64-efi/all_video.mod
/usr/lib64/grub/x86_64-efi/all_video.module
/usr/lib64/grub/x86_64-efi/aout.mod
/usr/lib64/grub/x86_64-efi/aout.module
/usr/lib64/grub/x86_64-efi/appleldr.mod
/usr/lib64/grub/x86_64-efi/appleldr.module
/usr/lib64/grub/x86_64-efi/archelp.mod
/usr/lib64/grub/x86_64-efi/archelp.module
/usr/lib64/grub/x86_64-efi/at_keyboard.mod
/usr/lib64/grub/x86_64-efi/at_keyboard.module
/usr/lib64/grub/x86_64-efi/ata.mod
/usr/lib64/grub/x86_64-efi/ata.module
/usr/lib64/grub/x86_64-efi/backtrace.mod
/usr/lib64/grub/x86_64-efi/backtrace.module
/usr/lib64/grub/x86_64-efi/bfs.mod
/usr/lib64/grub/x86_64-efi/bfs.module
/usr/lib64/grub/x86_64-efi/bitmap.mod
/usr/lib64/grub/x86_64-efi/bitmap.module
/usr/lib64/grub/x86_64-efi/bitmap_scale.mod
/usr/lib64/grub/x86_64-efi/bitmap_scale.module
/usr/lib64/grub/x86_64-efi/blocklist.mod
/usr/lib64/grub/x86_64-efi/blocklist.module
/usr/lib64/grub/x86_64-efi/boot.mod
/usr/lib64/grub/x86_64-efi/boot.module
/usr/lib64/grub/x86_64-efi/bsd.mod
/usr/lib64/grub/x86_64-efi/bsd.module
/usr/lib64/grub/x86_64-efi/btrfs.mod
/usr/lib64/grub/x86_64-efi/btrfs.module
/usr/lib64/grub/x86_64-efi/bufio.mod
/usr/lib64/grub/x86_64-efi/bufio.module
/usr/lib64/grub/x86_64-efi/cat.mod
/usr/lib64/grub/x86_64-efi/cat.module
/usr/lib64/grub/x86_64-efi/cbfs.mod
/usr/lib64/grub/x86_64-efi/cbfs.module
/usr/lib64/grub/x86_64-efi/cbls.mod
/usr/lib64/grub/x86_64-efi/cbls.module
/usr/lib64/grub/x86_64-efi/cbmemc.mod
/usr/lib64/grub/x86_64-efi/cbmemc.module
/usr/lib64/grub/x86_64-efi/cbtable.mod
/usr/lib64/grub/x86_64-efi/cbtable.module
/usr/lib64/grub/x86_64-efi/cbtime.mod
/usr/lib64/grub/x86_64-efi/cbtime.module
/usr/lib64/grub/x86_64-efi/chain.mod
/usr/lib64/grub/x86_64-efi/chain.module
/usr/lib64/grub/x86_64-efi/cmdline_cat_test.mod
/usr/lib64/grub/x86_64-efi/cmdline_cat_test.module
/usr/lib64/grub/x86_64-efi/cmp.mod
/usr/lib64/grub/x86_64-efi/cmp.module
/usr/lib64/grub/x86_64-efi/command.lst
/usr/lib64/grub/x86_64-efi/config.h
/usr/lib64/grub/x86_64-efi/configfile.mod
/usr/lib64/grub/x86_64-efi/configfile.module
/usr/lib64/grub/x86_64-efi/cpio.mod
/usr/lib64/grub/x86_64-efi/cpio.module
/usr/lib64/grub/x86_64-efi/cpio_be.mod
/usr/lib64/grub/x86_64-efi/cpio_be.module
/usr/lib64/grub/x86_64-efi/cpuid.mod
/usr/lib64/grub/x86_64-efi/cpuid.module
/usr/lib64/grub/x86_64-efi/crc64.mod
/usr/lib64/grub/x86_64-efi/crc64.module
/usr/lib64/grub/x86_64-efi/crypto.lst
/usr/lib64/grub/x86_64-efi/crypto.mod
/usr/lib64/grub/x86_64-efi/crypto.module
/usr/lib64/grub/x86_64-efi/cryptodisk.mod
/usr/lib64/grub/x86_64-efi/cryptodisk.module
/usr/lib64/grub/x86_64-efi/cs5536.mod
/usr/lib64/grub/x86_64-efi/cs5536.module
/usr/lib64/grub/x86_64-efi/date.mod
/usr/lib64/grub/x86_64-efi/date.module
/usr/lib64/grub/x86_64-efi/datehook.mod
/usr/lib64/grub/x86_64-efi/datehook.module
/usr/lib64/grub/x86_64-efi/datetime.mod
/usr/lib64/grub/x86_64-efi/datetime.module
/usr/lib64/grub/x86_64-efi/disk.mod
/usr/lib64/grub/x86_64-efi/disk.module
/usr/lib64/grub/x86_64-efi/diskfilter.mod
/usr/lib64/grub/x86_64-efi/diskfilter.module
/usr/lib64/grub/x86_64-efi/div_test.mod
/usr/lib64/grub/x86_64-efi/div_test.module
/usr/lib64/grub/x86_64-efi/dm_nv.mod
/usr/lib64/grub/x86_64-efi/dm_nv.module
/usr/lib64/grub/x86_64-efi/echo.mod
/usr/lib64/grub/x86_64-efi/echo.module
/usr/lib64/grub/x86_64-efi/efi_gop.mod
/usr/lib64/grub/x86_64-efi/efi_gop.module
/usr/lib64/grub/x86_64-efi/efi_uga.mod
/usr/lib64/grub/x86_64-efi/efi_uga.module
/usr/lib64/grub/x86_64-efi/efifwsetup.mod
/usr/lib64/grub/x86_64-efi/efifwsetup.module
/usr/lib64/grub/x86_64-efi/efinet.mod
/usr/lib64/grub/x86_64-efi/efinet.module
/usr/lib64/grub/x86_64-efi/ehci.mod
/usr/lib64/grub/x86_64-efi/ehci.module
/usr/lib64/grub/x86_64-efi/elf.mod
/usr/lib64/grub/x86_64-efi/elf.module
/usr/lib64/grub/x86_64-efi/eval.mod
/usr/lib64/grub/x86_64-efi/eval.module
/usr/lib64/grub/x86_64-efi/exfat.mod
/usr/lib64/grub/x86_64-efi/exfat.module
/usr/lib64/grub/x86_64-efi/exfctest.mod
/usr/lib64/grub/x86_64-efi/exfctest.module
/usr/lib64/grub/x86_64-efi/ext2.mod
/usr/lib64/grub/x86_64-efi/ext2.module
/usr/lib64/grub/x86_64-efi/extcmd.mod
/usr/lib64/grub/x86_64-efi/extcmd.module
/usr/lib64/grub/x86_64-efi/fat.mod
/usr/lib64/grub/x86_64-efi/fat.module
/usr/lib64/grub/x86_64-efi/file.mod
/usr/lib64/grub/x86_64-efi/file.module
/usr/lib64/grub/x86_64-efi/fixvideo.mod
/usr/lib64/grub/x86_64-efi/fixvideo.module
/usr/lib64/grub/x86_64-efi/font.mod
/usr/lib64/grub/x86_64-efi/font.module
/usr/lib64/grub/x86_64-efi/fs.lst
/usr/lib64/grub/x86_64-efi/fshelp.mod
/usr/lib64/grub/x86_64-efi/fshelp.module
/usr/lib64/grub/x86_64-efi/functional_test.mod
/usr/lib64/grub/x86_64-efi/functional_test.module
/usr/lib64/grub/x86_64-efi/gcry_arcfour.mod
/usr/lib64/grub/x86_64-efi/gcry_arcfour.module
/usr/lib64/grub/x86_64-efi/gcry_blowfish.mod
/usr/lib64/grub/x86_64-efi/gcry_blowfish.module
/usr/lib64/grub/x86_64-efi/gcry_camellia.mod
/usr/lib64/grub/x86_64-efi/gcry_camellia.module
/usr/lib64/grub/x86_64-efi/gcry_cast5.mod
/usr/lib64/grub/x86_64-efi/gcry_cast5.module
/usr/lib64/grub/x86_64-efi/gcry_crc.mod
/usr/lib64/grub/x86_64-efi/gcry_crc.module
/usr/lib64/grub/x86_64-efi/gcry_des.mod
/usr/lib64/grub/x86_64-efi/gcry_des.module
/usr/lib64/grub/x86_64-efi/gcry_dsa.mod
/usr/lib64/grub/x86_64-efi/gcry_dsa.module
/usr/lib64/grub/x86_64-efi/gcry_idea.mod
/usr/lib64/grub/x86_64-efi/gcry_idea.module
/usr/lib64/grub/x86_64-efi/gcry_md4.mod
/usr/lib64/grub/x86_64-efi/gcry_md4.module
/usr/lib64/grub/x86_64-efi/gcry_md5.mod
/usr/lib64/grub/x86_64-efi/gcry_md5.module
/usr/lib64/grub/x86_64-efi/gcry_rfc2268.mod
/usr/lib64/grub/x86_64-efi/gcry_rfc2268.module
/usr/lib64/grub/x86_64-efi/gcry_rijndael.mod
/usr/lib64/grub/x86_64-efi/gcry_rijndael.module
/usr/lib64/grub/x86_64-efi/gcry_rmd160.mod
/usr/lib64/grub/x86_64-efi/gcry_rmd160.module
/usr/lib64/grub/x86_64-efi/gcry_rsa.mod
/usr/lib64/grub/x86_64-efi/gcry_rsa.module
/usr/lib64/grub/x86_64-efi/gcry_seed.mod
/usr/lib64/grub/x86_64-efi/gcry_seed.module
/usr/lib64/grub/x86_64-efi/gcry_serpent.mod
/usr/lib64/grub/x86_64-efi/gcry_serpent.module
/usr/lib64/grub/x86_64-efi/gcry_sha1.mod
/usr/lib64/grub/x86_64-efi/gcry_sha1.module
/usr/lib64/grub/x86_64-efi/gcry_sha256.mod
/usr/lib64/grub/x86_64-efi/gcry_sha256.module
/usr/lib64/grub/x86_64-efi/gcry_sha512.mod
/usr/lib64/grub/x86_64-efi/gcry_sha512.module
/usr/lib64/grub/x86_64-efi/gcry_tiger.mod
/usr/lib64/grub/x86_64-efi/gcry_tiger.module
/usr/lib64/grub/x86_64-efi/gcry_twofish.mod
/usr/lib64/grub/x86_64-efi/gcry_twofish.module
/usr/lib64/grub/x86_64-efi/gcry_whirlpool.mod
/usr/lib64/grub/x86_64-efi/gcry_whirlpool.module
/usr/lib64/grub/x86_64-efi/gdb_grub
/usr/lib64/grub/x86_64-efi/geli.mod
/usr/lib64/grub/x86_64-efi/geli.module
/usr/lib64/grub/x86_64-efi/gettext.mod
/usr/lib64/grub/x86_64-efi/gettext.module
/usr/lib64/grub/x86_64-efi/gfxmenu.mod
/usr/lib64/grub/x86_64-efi/gfxmenu.module
/usr/lib64/grub/x86_64-efi/gfxterm.mod
/usr/lib64/grub/x86_64-efi/gfxterm.module
/usr/lib64/grub/x86_64-efi/gfxterm_background.mod
/usr/lib64/grub/x86_64-efi/gfxterm_background.module
/usr/lib64/grub/x86_64-efi/gfxterm_menu.mod
/usr/lib64/grub/x86_64-efi/gfxterm_menu.module
/usr/lib64/grub/x86_64-efi/gmodule.pl
/usr/lib64/grub/x86_64-efi/gptsync.mod
/usr/lib64/grub/x86_64-efi/gptsync.module
/usr/lib64/grub/x86_64-efi/gzio.mod
/usr/lib64/grub/x86_64-efi/gzio.module
/usr/lib64/grub/x86_64-efi/halt.mod
/usr/lib64/grub/x86_64-efi/halt.module
/usr/lib64/grub/x86_64-efi/hashsum.mod
/usr/lib64/grub/x86_64-efi/hashsum.module
/usr/lib64/grub/x86_64-efi/hdparm.mod
/usr/lib64/grub/x86_64-efi/hdparm.module
/usr/lib64/grub/x86_64-efi/hello.mod
/usr/lib64/grub/x86_64-efi/hello.module
/usr/lib64/grub/x86_64-efi/help.mod
/usr/lib64/grub/x86_64-efi/help.module
/usr/lib64/grub/x86_64-efi/hexdump.mod
/usr/lib64/grub/x86_64-efi/hexdump.module
/usr/lib64/grub/x86_64-efi/hfs.mod
/usr/lib64/grub/x86_64-efi/hfs.module
/usr/lib64/grub/x86_64-efi/hfsplus.mod
/usr/lib64/grub/x86_64-efi/hfsplus.module
/usr/lib64/grub/x86_64-efi/hfspluscomp.mod
/usr/lib64/grub/x86_64-efi/hfspluscomp.module
/usr/lib64/grub/x86_64-efi/http.mod
/usr/lib64/grub/x86_64-efi/http.module
/usr/lib64/grub/x86_64-efi/iorw.mod
/usr/lib64/grub/x86_64-efi/iorw.module
/usr/lib64/grub/x86_64-efi/iso9660.mod
/usr/lib64/grub/x86_64-efi/iso9660.module
/usr/lib64/grub/x86_64-efi/jfs.mod
/usr/lib64/grub/x86_64-efi/jfs.module
/usr/lib64/grub/x86_64-efi/jpeg.mod
/usr/lib64/grub/x86_64-efi/jpeg.module
/usr/lib64/grub/x86_64-efi/kernel.exec
/usr/lib64/grub/x86_64-efi/kernel.img
/usr/lib64/grub/x86_64-efi/keylayouts.mod
/usr/lib64/grub/x86_64-efi/keylayouts.module
/usr/lib64/grub/x86_64-efi/keystatus.mod
/usr/lib64/grub/x86_64-efi/keystatus.module
/usr/lib64/grub/x86_64-efi/ldm.mod
/usr/lib64/grub/x86_64-efi/ldm.module
/usr/lib64/grub/x86_64-efi/legacy_password_test.mod
/usr/lib64/grub/x86_64-efi/legacy_password_test.module
/usr/lib64/grub/x86_64-efi/legacycfg.mod
/usr/lib64/grub/x86_64-efi/legacycfg.module
/usr/lib64/grub/x86_64-efi/linux.mod
/usr/lib64/grub/x86_64-efi/linux.module
/usr/lib64/grub/x86_64-efi/linux16.mod
/usr/lib64/grub/x86_64-efi/linux16.module
/usr/lib64/grub/x86_64-efi/linuxefi.mod
/usr/lib64/grub/x86_64-efi/linuxefi.module
/usr/lib64/grub/x86_64-efi/loadbios.mod
/usr/lib64/grub/x86_64-efi/loadbios.module
/usr/lib64/grub/x86_64-efi/loadenv.mod
/usr/lib64/grub/x86_64-efi/loadenv.module
/usr/lib64/grub/x86_64-efi/loopback.mod
/usr/lib64/grub/x86_64-efi/loopback.module
/usr/lib64/grub/x86_64-efi/ls.mod
/usr/lib64/grub/x86_64-efi/ls.module
/usr/lib64/grub/x86_64-efi/lsacpi.mod
/usr/lib64/grub/x86_64-efi/lsacpi.module
/usr/lib64/grub/x86_64-efi/lsefi.mod
/usr/lib64/grub/x86_64-efi/lsefi.module
/usr/lib64/grub/x86_64-efi/lsefimmap.mod
/usr/lib64/grub/x86_64-efi/lsefimmap.module
/usr/lib64/grub/x86_64-efi/lsefisystab.mod
/usr/lib64/grub/x86_64-efi/lsefisystab.module
/usr/lib64/grub/x86_64-efi/lsmmap.mod
/usr/lib64/grub/x86_64-efi/lsmmap.module
/usr/lib64/grub/x86_64-efi/lspci.mod
/usr/lib64/grub/x86_64-efi/lspci.module
/usr/lib64/grub/x86_64-efi/lssal.mod
/usr/lib64/grub/x86_64-efi/lssal.module
/usr/lib64/grub/x86_64-efi/luks.mod
/usr/lib64/grub/x86_64-efi/luks.module
/usr/lib64/grub/x86_64-efi/lvm.mod
/usr/lib64/grub/x86_64-efi/lvm.module
/usr/lib64/grub/x86_64-efi/lzopio.mod
/usr/lib64/grub/x86_64-efi/lzopio.module
/usr/lib64/grub/x86_64-efi/macbless.mod
/usr/lib64/grub/x86_64-efi/macbless.module
/usr/lib64/grub/x86_64-efi/macho.mod
/usr/lib64/grub/x86_64-efi/macho.module
/usr/lib64/grub/x86_64-efi/mdraid09.mod
/usr/lib64/grub/x86_64-efi/mdraid09.module
/usr/lib64/grub/x86_64-efi/mdraid09_be.mod
/usr/lib64/grub/x86_64-efi/mdraid09_be.module
/usr/lib64/grub/x86_64-efi/mdraid1x.mod
/usr/lib64/grub/x86_64-efi/mdraid1x.module
/usr/lib64/grub/x86_64-efi/memdisk.mod
/usr/lib64/grub/x86_64-efi/memdisk.module
/usr/lib64/grub/x86_64-efi/memrw.mod
/usr/lib64/grub/x86_64-efi/memrw.module
/usr/lib64/grub/x86_64-efi/minicmd.mod
/usr/lib64/grub/x86_64-efi/minicmd.module
/usr/lib64/grub/x86_64-efi/minix.mod
/usr/lib64/grub/x86_64-efi/minix.module
/usr/lib64/grub/x86_64-efi/minix2.mod
/usr/lib64/grub/x86_64-efi/minix2.module
/usr/lib64/grub/x86_64-efi/minix2_be.mod
/usr/lib64/grub/x86_64-efi/minix2_be.module
/usr/lib64/grub/x86_64-efi/minix3.mod
/usr/lib64/grub/x86_64-efi/minix3.module
/usr/lib64/grub/x86_64-efi/minix3_be.mod
/usr/lib64/grub/x86_64-efi/minix3_be.module
/usr/lib64/grub/x86_64-efi/minix_be.mod
/usr/lib64/grub/x86_64-efi/minix_be.module
/usr/lib64/grub/x86_64-efi/mmap.mod
/usr/lib64/grub/x86_64-efi/mmap.module
/usr/lib64/grub/x86_64-efi/moddep.lst
/usr/lib64/grub/x86_64-efi/modinfo.sh
/usr/lib64/grub/x86_64-efi/morse.mod
/usr/lib64/grub/x86_64-efi/morse.module
/usr/lib64/grub/x86_64-efi/mpi.mod
/usr/lib64/grub/x86_64-efi/mpi.module
/usr/lib64/grub/x86_64-efi/msdospart.mod
/usr/lib64/grub/x86_64-efi/msdospart.module
/usr/lib64/grub/x86_64-efi/multiboot.mod
/usr/lib64/grub/x86_64-efi/multiboot.module
/usr/lib64/grub/x86_64-efi/multiboot2.mod
/usr/lib64/grub/x86_64-efi/multiboot2.module
/usr/lib64/grub/x86_64-efi/nativedisk.mod
/usr/lib64/grub/x86_64-efi/nativedisk.module
/usr/lib64/grub/x86_64-efi/net.mod
/usr/lib64/grub/x86_64-efi/net.module
/usr/lib64/grub/x86_64-efi/newc.mod
/usr/lib64/grub/x86_64-efi/newc.module
/usr/lib64/grub/x86_64-efi/nilfs2.mod
/usr/lib64/grub/x86_64-efi/nilfs2.module
/usr/lib64/grub/x86_64-efi/normal.mod
/usr/lib64/grub/x86_64-efi/normal.module
/usr/lib64/grub/x86_64-efi/ntfs.mod
/usr/lib64/grub/x86_64-efi/ntfs.module
/usr/lib64/grub/x86_64-efi/ntfscomp.mod
/usr/lib64/grub/x86_64-efi/ntfscomp.module
/usr/lib64/grub/x86_64-efi/odc.mod
/usr/lib64/grub/x86_64-efi/odc.module
/usr/lib64/grub/x86_64-efi/offsetio.mod
/usr/lib64/grub/x86_64-efi/offsetio.module
/usr/lib64/grub/x86_64-efi/ohci.mod
/usr/lib64/grub/x86_64-efi/ohci.module
/usr/lib64/grub/x86_64-efi/part_acorn.mod
/usr/lib64/grub/x86_64-efi/part_acorn.module
/usr/lib64/grub/x86_64-efi/part_amiga.mod
/usr/lib64/grub/x86_64-efi/part_amiga.module
/usr/lib64/grub/x86_64-efi/part_apple.mod
/usr/lib64/grub/x86_64-efi/part_apple.module
/usr/lib64/grub/x86_64-efi/part_bsd.mod
/usr/lib64/grub/x86_64-efi/part_bsd.module
/usr/lib64/grub/x86_64-efi/part_dfly.mod
/usr/lib64/grub/x86_64-efi/part_dfly.module
/usr/lib64/grub/x86_64-efi/part_dvh.mod
/usr/lib64/grub/x86_64-efi/part_dvh.module
/usr/lib64/grub/x86_64-efi/part_gpt.mod
/usr/lib64/grub/x86_64-efi/part_gpt.module
/usr/lib64/grub/x86_64-efi/part_msdos.mod
/usr/lib64/grub/x86_64-efi/part_msdos.module
/usr/lib64/grub/x86_64-efi/part_plan.mod
/usr/lib64/grub/x86_64-efi/part_plan.module
/usr/lib64/grub/x86_64-efi/part_sun.mod
/usr/lib64/grub/x86_64-efi/part_sun.module
/usr/lib64/grub/x86_64-efi/part_sunpc.mod
/usr/lib64/grub/x86_64-efi/part_sunpc.module
/usr/lib64/grub/x86_64-efi/partmap.lst
/usr/lib64/grub/x86_64-efi/parttool.lst
/usr/lib64/grub/x86_64-efi/parttool.mod
/usr/lib64/grub/x86_64-efi/parttool.module
/usr/lib64/grub/x86_64-efi/password.mod
/usr/lib64/grub/x86_64-efi/password.module
/usr/lib64/grub/x86_64-efi/password_pbkdf2.mod
/usr/lib64/grub/x86_64-efi/password_pbkdf2.module
/usr/lib64/grub/x86_64-efi/pata.mod
/usr/lib64/grub/x86_64-efi/pata.module
/usr/lib64/grub/x86_64-efi/pbkdf2.mod
/usr/lib64/grub/x86_64-efi/pbkdf2.module
/usr/lib64/grub/x86_64-efi/pbkdf2_test.mod
/usr/lib64/grub/x86_64-efi/pbkdf2_test.module
/usr/lib64/grub/x86_64-efi/pcidump.mod
/usr/lib64/grub/x86_64-efi/pcidump.module
/usr/lib64/grub/x86_64-efi/play.mod
/usr/lib64/grub/x86_64-efi/play.module
/usr/lib64/grub/x86_64-efi/png.mod
/usr/lib64/grub/x86_64-efi/png.module
/usr/lib64/grub/x86_64-efi/priority_queue.mod
/usr/lib64/grub/x86_64-efi/priority_queue.module
/usr/lib64/grub/x86_64-efi/probe.mod
/usr/lib64/grub/x86_64-efi/probe.module
/usr/lib64/grub/x86_64-efi/procfs.mod
/usr/lib64/grub/x86_64-efi/procfs.module
/usr/lib64/grub/x86_64-efi/progress.mod
/usr/lib64/grub/x86_64-efi/progress.module
/usr/lib64/grub/x86_64-efi/raid5rec.mod
/usr/lib64/grub/x86_64-efi/raid5rec.module
/usr/lib64/grub/x86_64-efi/raid6rec.mod
/usr/lib64/grub/x86_64-efi/raid6rec.module
/usr/lib64/grub/x86_64-efi/read.mod
/usr/lib64/grub/x86_64-efi/read.module
/usr/lib64/grub/x86_64-efi/reboot.mod
/usr/lib64/grub/x86_64-efi/reboot.module
/usr/lib64/grub/x86_64-efi/regexp.mod
/usr/lib64/grub/x86_64-efi/regexp.module
/usr/lib64/grub/x86_64-efi/reiserfs.mod
/usr/lib64/grub/x86_64-efi/reiserfs.module
/usr/lib64/grub/x86_64-efi/relocator.mod
/usr/lib64/grub/x86_64-efi/relocator.module
/usr/lib64/grub/x86_64-efi/romfs.mod
/usr/lib64/grub/x86_64-efi/romfs.module
/usr/lib64/grub/x86_64-efi/scsi.mod
/usr/lib64/grub/x86_64-efi/scsi.module
/usr/lib64/grub/x86_64-efi/search.mod
/usr/lib64/grub/x86_64-efi/search.module
/usr/lib64/grub/x86_64-efi/search_fs_file.mod
/usr/lib64/grub/x86_64-efi/search_fs_file.module
/usr/lib64/grub/x86_64-efi/search_fs_uuid.mod
/usr/lib64/grub/x86_64-efi/search_fs_uuid.module
/usr/lib64/grub/x86_64-efi/search_label.mod
/usr/lib64/grub/x86_64-efi/search_label.module
/usr/lib64/grub/x86_64-efi/serial.mod
/usr/lib64/grub/x86_64-efi/serial.module
/usr/lib64/grub/x86_64-efi/setjmp.mod
/usr/lib64/grub/x86_64-efi/setjmp.module
/usr/lib64/grub/x86_64-efi/setjmp_test.mod
/usr/lib64/grub/x86_64-efi/setjmp_test.module
/usr/lib64/grub/x86_64-efi/setpci.mod
/usr/lib64/grub/x86_64-efi/setpci.module
/usr/lib64/grub/x86_64-efi/sfs.mod
/usr/lib64/grub/x86_64-efi/sfs.module
/usr/lib64/grub/x86_64-efi/signature_test.mod
/usr/lib64/grub/x86_64-efi/signature_test.module
/usr/lib64/grub/x86_64-efi/sleep.mod
/usr/lib64/grub/x86_64-efi/sleep.module
/usr/lib64/grub/x86_64-efi/sleep_test.mod
/usr/lib64/grub/x86_64-efi/sleep_test.module
/usr/lib64/grub/x86_64-efi/spkmodem.mod
/usr/lib64/grub/x86_64-efi/spkmodem.module
/usr/lib64/grub/x86_64-efi/squash4.mod
/usr/lib64/grub/x86_64-efi/squash4.module
/usr/lib64/grub/x86_64-efi/syslinuxcfg.mod
/usr/lib64/grub/x86_64-efi/syslinuxcfg.module
/usr/lib64/grub/x86_64-efi/tar.mod
/usr/lib64/grub/x86_64-efi/tar.module
/usr/lib64/grub/x86_64-efi/terminal.lst
/usr/lib64/grub/x86_64-efi/terminal.mod
/usr/lib64/grub/x86_64-efi/terminal.module
/usr/lib64/grub/x86_64-efi/terminfo.mod
/usr/lib64/grub/x86_64-efi/terminfo.module
/usr/lib64/grub/x86_64-efi/test.mod
/usr/lib64/grub/x86_64-efi/test.module
/usr/lib64/grub/x86_64-efi/test_blockarg.mod
/usr/lib64/grub/x86_64-efi/test_blockarg.module
/usr/lib64/grub/x86_64-efi/testload.mod
/usr/lib64/grub/x86_64-efi/testload.module
/usr/lib64/grub/x86_64-efi/testspeed.mod
/usr/lib64/grub/x86_64-efi/testspeed.module
/usr/lib64/grub/x86_64-efi/tftp.mod
/usr/lib64/grub/x86_64-efi/tftp.module
/usr/lib64/grub/x86_64-efi/tga.mod
/usr/lib64/grub/x86_64-efi/tga.module
/usr/lib64/grub/x86_64-efi/time.mod
/usr/lib64/grub/x86_64-efi/time.module
/usr/lib64/grub/x86_64-efi/tr.mod
/usr/lib64/grub/x86_64-efi/tr.module
/usr/lib64/grub/x86_64-efi/trig.mod
/usr/lib64/grub/x86_64-efi/trig.module
/usr/lib64/grub/x86_64-efi/true.mod
/usr/lib64/grub/x86_64-efi/true.module
/usr/lib64/grub/x86_64-efi/udf.mod
/usr/lib64/grub/x86_64-efi/udf.module
/usr/lib64/grub/x86_64-efi/ufs1.mod
/usr/lib64/grub/x86_64-efi/ufs1.module
/usr/lib64/grub/x86_64-efi/ufs1_be.mod
/usr/lib64/grub/x86_64-efi/ufs1_be.module
/usr/lib64/grub/x86_64-efi/ufs2.mod
/usr/lib64/grub/x86_64-efi/ufs2.module
/usr/lib64/grub/x86_64-efi/uhci.mod
/usr/lib64/grub/x86_64-efi/uhci.module
/usr/lib64/grub/x86_64-efi/usb.mod
/usr/lib64/grub/x86_64-efi/usb.module
/usr/lib64/grub/x86_64-efi/usb_keyboard.mod
/usr/lib64/grub/x86_64-efi/usb_keyboard.module
/usr/lib64/grub/x86_64-efi/usbms.mod
/usr/lib64/grub/x86_64-efi/usbms.module
/usr/lib64/grub/x86_64-efi/usbserial_common.mod
/usr/lib64/grub/x86_64-efi/usbserial_common.module
/usr/lib64/grub/x86_64-efi/usbserial_ftdi.mod
/usr/lib64/grub/x86_64-efi/usbserial_ftdi.module
/usr/lib64/grub/x86_64-efi/usbserial_pl2303.mod
/usr/lib64/grub/x86_64-efi/usbserial_pl2303.module
/usr/lib64/grub/x86_64-efi/usbserial_usbdebug.mod
/usr/lib64/grub/x86_64-efi/usbserial_usbdebug.module
/usr/lib64/grub/x86_64-efi/usbtest.mod
/usr/lib64/grub/x86_64-efi/usbtest.module
/usr/lib64/grub/x86_64-efi/verify.mod
/usr/lib64/grub/x86_64-efi/verify.module
/usr/lib64/grub/x86_64-efi/video.lst
/usr/lib64/grub/x86_64-efi/video.mod
/usr/lib64/grub/x86_64-efi/video.module
/usr/lib64/grub/x86_64-efi/video_bochs.mod
/usr/lib64/grub/x86_64-efi/video_bochs.module
/usr/lib64/grub/x86_64-efi/video_cirrus.mod
/usr/lib64/grub/x86_64-efi/video_cirrus.module
/usr/lib64/grub/x86_64-efi/video_colors.mod
/usr/lib64/grub/x86_64-efi/video_colors.module
/usr/lib64/grub/x86_64-efi/video_fb.mod
/usr/lib64/grub/x86_64-efi/video_fb.module
/usr/lib64/grub/x86_64-efi/videoinfo.mod
/usr/lib64/grub/x86_64-efi/videoinfo.module
/usr/lib64/grub/x86_64-efi/videotest.mod
/usr/lib64/grub/x86_64-efi/videotest.module
/usr/lib64/grub/x86_64-efi/videotest_checksum.mod
/usr/lib64/grub/x86_64-efi/videotest_checksum.module
/usr/lib64/grub/x86_64-efi/xfs.mod
/usr/lib64/grub/x86_64-efi/xfs.module
/usr/lib64/grub/x86_64-efi/xnu.mod
/usr/lib64/grub/x86_64-efi/xnu.module
/usr/lib64/grub/x86_64-efi/xnu_uuid.mod
/usr/lib64/grub/x86_64-efi/xnu_uuid.module
/usr/lib64/grub/x86_64-efi/xnu_uuid_test.mod
/usr/lib64/grub/x86_64-efi/xnu_uuid_test.module
/usr/lib64/grub/x86_64-efi/xzio.mod
/usr/lib64/grub/x86_64-efi/xzio.module
/usr/lib64/grub/x86_64-efi/zfs.mod
/usr/lib64/grub/x86_64-efi/zfs.module
/usr/lib64/grub/x86_64-efi/zfscrypt.mod
/usr/lib64/grub/x86_64-efi/zfscrypt.module
/usr/lib64/grub/x86_64-efi/zfsinfo.mod
/usr/lib64/grub/x86_64-efi/zfsinfo.module

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/grub-mkfont
/usr/bin/grub-bios-setup
/usr/bin/grub-editenv
/usr/bin/grub-file
/usr/bin/grub-fstest
/usr/bin/grub-glue-efi
/usr/bin/grub-install
/usr/bin/grub-kbdcomp
/usr/bin/grub-macbless
/usr/bin/grub-menulst2cfg
/usr/bin/grub-mkconfig
/usr/bin/grub-mkimage
/usr/bin/grub-mklayout
/usr/bin/grub-mknetdir
/usr/bin/grub-mkpasswd-pbkdf2
/usr/bin/grub-mkrelpath
/usr/bin/grub-mkrescue
/usr/bin/grub-mkstandalone
/usr/bin/grub-ofpathname
/usr/bin/grub-probe
/usr/bin/grub-reboot
/usr/bin/grub-render-label
/usr/bin/grub-script-check
/usr/bin/grub-set-default
/usr/bin/grub-sparc64-setup
/usr/bin/grub-syslinux2cfg

%files data
%defattr(-,root,root,-)
/usr/share/grub/grub-mkconfig_lib

%files doc
%defattr(-,root,root,-)
%doc /usr/share/info/*
%doc /usr/share/man/man1/*
%doc /usr/share/man/man8/*

%files extras
%defattr(-,root,root,-)
/usr/bin/grub-mkfont
