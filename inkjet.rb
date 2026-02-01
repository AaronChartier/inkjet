class Inkjet < Formula
  include Language::Python::Virtualenv

  desc "CLI tool for Bluetooth thermal printer control and printing"
  homepage "https://github.com/AaronChartier/inkjet"
  url "https://github.com/AaronChartier/inkjet/archive/refs/tags/v0.1.0.tar.gz"
  sha256 "8923c26ee5492ddcb13418b31ed10421ac377340fab21e61ab925d978d0a4e11"
  license "MIT"

  depends_on "python@3.12"

  def install
    virtualenv_install_with_resources
  end

  test do
    # Simple test to verify the version command works
    assert_match "0.1.0", shell_output("#{bin}/inkjet --version")
  end
end